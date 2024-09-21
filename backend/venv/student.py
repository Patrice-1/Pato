import sqlite3

# Function to create the SQLite database and the students table
def create_student_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    # Create students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_student_database()
    print("Database 'students.db' created with the 'students' table.")
