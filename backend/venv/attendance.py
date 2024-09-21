import sqlite3

def create_database():
    # Connect to SQLite (or create it if it doesn't exist)
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    # Create table for Students
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Create table for Attendance Records
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            attendance_date DATE NOT NULL,
            status TEXT CHECK(status IN ('present', 'absent')) NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Students (id)
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database 'attendance.db' created with Students and Attendance tables.")

if __name__ == "__main__":
    create_database()
