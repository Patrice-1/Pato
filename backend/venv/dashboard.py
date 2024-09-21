import sqlite3

# Function to create the SQLite database and the necessary tables
def create_dashboard_database():
    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('school_dashboard.db')
    cursor = conn.cursor()

    # Create teachers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            subject TEXT,
            grade TEXT,
            attendance TEXT,
            grade_date TEXT,
            attendance_date TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES teachers (id) ON DELETE CASCADE
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_dashboard_database()
    print("Database 'school_dashboard.db' created with the 'teachers' and 'students' tables.")
