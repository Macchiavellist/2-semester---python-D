import psycopg2
import csv

conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    ''')
    conn.commit()

def insert_from_console():
    name = input()
    phone = input()
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

if __name__ == "__main__":
    create_table()
    # insert_from_console()
    # insert_from_csv("contacts.csv")
    # update_entry("Alice", "123456789")
    # query_data("Ali")
    # delete_entry("Alice")

cur.close()
conn.close()
