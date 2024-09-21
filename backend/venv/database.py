import sqlite3

def create_master_database():
    # Connect to the master SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect('school_management_master.db')
    cursor = conn.cursor()

    # Create table for Principals
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Principals (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create table for Teachers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create table for Students
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject TEXT,
            grade TEXT,
            attendance TEXT,
            grade_date TEXT,
            attendance_date TEXT,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES Teachers (id) ON DELETE SET NULL
        )
    ''')

    # Create table for Attendance Records
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            attendance_date DATE NOT NULL,
            status TEXT CHECK(status IN ('present', 'absent')) NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE CASCADE
        )
    ''')

    # Create table for Grades
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            subject TEXT NOT NULL,
            grade TEXT NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE CASCADE
        )
    ''')

    # Create users table for authentication
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            user_type TEXT CHECK(user_type IN ('principal', 'teacher')) NOT NULL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Master database 'school_management_master.db' created with all necessary tables.")

if __name__ == "__main__":
    create_master_database()
