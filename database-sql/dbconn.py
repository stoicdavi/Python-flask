import sqlite3 as sql

def initialize_db():
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            addr TEXT NOT NULL,
            city TEXT NOT NULL,
            pin TEXT NOT NULL
        );
    ''')
    con.commit()
    con.close()

if __name__ == '__main__':
    initialize_db()
