import psycopg2
import csv

# Подключение к БД
conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


# Создание таблицы
def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    ''')
    conn.commit()


# Создание всех процедур и функций
def create_procedures_and_functions():
    cur.execute("""
    CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern TEXT)
    RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook
        WHERE name ILIKE '%' || pattern || '%' OR phone ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
            UPDATE phonebook SET phone = p_phone WHERE name = p_name;
        ELSE
            INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
        END IF;
    END;
    $$;
    """)

    cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_many_users(
        IN user_list TEXT[][],
        OUT invalid_users TEXT[][]
    )
    LANGUAGE plpgsql AS $$
    DECLARE
        i INT;
        username TEXT;
        userphone TEXT;
        invalids TEXT[][];
    BEGIN
        invalids := ARRAY[]::TEXT[][];
        FOR i IN 1 .. array_length(user_list, 1) LOOP
            username := user_list[i][1];
            userphone := user_list[i][2];
            IF userphone ~ '^\d+$' THEN
                CALL insert_or_update_user(username, userphone);
            ELSE
                invalids := array_append(invalids, ARRAY[username, userphone]);
            END IF;
        END LOOP;
        invalid_users := invalids;
    END;
    $$;
    """)

    cur.execute("""
    CREATE OR REPLACE FUNCTION get_paginated_data(p_limit INT, p_offset INT)
    RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
    BEGIN
        RETURN QUERY
        SELECT * FROM phonebook ORDER BY id LIMIT p_limit OFFSET p_offset;
    END;
    $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
    CREATE OR REPLACE PROCEDURE delete_by_user_or_phone(p_identifier TEXT)
    LANGUAGE plpgsql AS $$
    BEGIN
        DELETE FROM phonebook WHERE name = p_identifier OR phone = p_identifier;
    END;
    $$;
    """)

    conn.commit()


# Обёртки Python
def call_get_records_by_pattern(pattern):
    cur.callproc('get_records_by_pattern', (pattern,))
    for row in cur.fetchall():
        print(row)


def call_insert_or_update_user(name, phone):
    cur.callproc('insert_or_update_user', (name, phone))
    conn.commit()


def call_insert_many_users(user_list):
    pg_array = [[user[0], user[1]] for user in user_list]
    cur.execute("CALL insert_many_users(%s)", (pg_array,))
    conn.commit()


def call_get_paginated_data(limit, offset):
    cur.callproc('get_paginated_data', (limit, offset))
    for row in cur.fetchall():
        print(row)


def call_delete_by_user_or_phone(identifier):
    cur.callproc('delete_by_user_or_phone', (identifier,))
    conn.commit()


# Старые функции
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()


def insert_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()


def update_entry(name, new_phone):
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()


def query_data(filter_val):
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f"%{filter_val}%", f"%{filter_val}%"))
    for row in cur.fetchall():
        print(row)


def delete_entry(identifier):
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (identifier, identifier))
    conn.commit()


# MAIN
if __name__ == "__main__":
    create_table()
    create_procedures_and_functions()

    # Тесты
    # call_insert_or_update_user("Alice", "123456")
    # call_insert_or_update_user("Bob", "987654")

    # call_insert_many_users([["John", "1111"], ["Eve", "abcd"], ["Tom", "2222"]])

    # call_get_records_by_pattern("Ali")
    # call_get_paginated_data(2, 0)
    # call_delete_by_user_or_phone("Bob")
    pass

# Завершаем
cur.close()
conn.close()
