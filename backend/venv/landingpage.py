import sqlite3

# Function to create a SQLite database
def create_database():
    # Connect to SQLite (or create it if it doesn't exist)
    conn = sqlite3.connect('school_management_system.db')
    cursor = conn.cursor()

    # Create tables for Principals and Teachers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Principals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database created and tables initialized.")

if __name__ == "__main__":
    create_database()
