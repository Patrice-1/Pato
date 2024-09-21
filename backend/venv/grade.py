import sqlite3

# Function to create the SQLite database and the grades table
def create_grades_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()

    # Create grades table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL CHECK(score >= 0 AND score <= 100),
            grade TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_grades_database()
    print("Database 'grades.db' created with the 'grades' table.")
