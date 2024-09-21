import sqlite3

# Function to create the SQLite database and the users table
def create_auth_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('auth.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            user_type TEXT CHECK(user_type IN ('principal', 'teacher')) NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_auth_database()
    print("Database 'auth.db' created with the 'users' table.")
