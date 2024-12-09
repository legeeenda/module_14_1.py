import sqlite3


db_path = "not_telegram.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
""")


cursor.execute("DELETE FROM Users")

users_data = [
    (f"User{i}", f"example{i}@gmail.com", i * 10, 1000) for i in range(1, 11)
]
cursor.executemany("""
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
""", users_data)


cursor.execute("""
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
""")


cursor.execute("""
DELETE FROM Users
WHERE id % 3 = 0
""")


cursor.execute("""
SELECT username, email, age, balance
FROM Users
WHERE age != 60
""")
results = cursor.fetchall()


formatted_output = [f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}" for row in results]


for line in formatted_output:
    print(line)

conn.commit()
conn.close()
