import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_user",
    password="your_password",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_tables():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE
        );
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INT REFERENCES users(id),
            score INT,
            level INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()

def get_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if not user:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        conn.commit()
        user = cur.fetchone()
    return user[0]

def get_latest_score(user_id):
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    return cur.fetchone()

def save_score(user_id, score, level):
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()

if __name__ == "__main__":
    create_tables()
    username = input()
    user_id = get_user(username)
    latest = get_latest_score(user_id)
    if latest:
        print(latest[0], latest[1])
    else:
        print("0 1")
    save_score(user_id, score=200, level=2)

cur.close()
conn.close()
