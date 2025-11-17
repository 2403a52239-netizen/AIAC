import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        description TEXT,
        location TEXT,
        image TEXT,
        status TEXT
    )''')
    conn.commit()
    conn.close()

def add_item(name, desc, location, image, status):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO items (name, description, location, image, status) VALUES (?, ?, ?, ?, ?)",
              (name, desc, location, image, status))
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    conn.close()
    return items

def delete_item(item_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()