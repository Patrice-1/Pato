from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
from typing import List, Optional
from datetime import date


app = FastAPI()

# CORS middleware configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

DATABASE = 'school_management_master.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


class Principal(BaseModel):
    id: Optional[int]  # Add id for updates and returns
    name: str
    email: str
    password: str


class Teacher(BaseModel):
    id: Optional[int]  # Add id for updates and returns
    name: str
    email: str
    password: str


class Student(BaseModel):
    id: Optional[int]  # Add id for updates and returns
    name: str
    subject: Optional[str] = None
    grade: Optional[str] = None
    teacher_id: Optional[int] = None


class Attendance(BaseModel):
    id: Optional[int]  # Add id for updates and returns
    student_id: int
    attendance_date: str
    status: str


class Grade(BaseModel):
    id: Optional[int]  # Add id for updates and returns
    student_id: int
    subject: str
    grade: float
    date: date


class User(BaseModel):
    id: Optional[int]  # Add id for updates and returns
    username: str
    password: str
    user_type: str


@app.post("/principals/", response_model=Principal)
def add_principal(principal: Principal):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Principals (name, email, password) VALUES (:name, :email, :password)",
            (principal.name, principal.email, principal.password),
        )
        conn.commit()
        principal.id = cursor.lastrowid  # Set the ID for the response
        return principal


@app.get("/principals/", response_model=List[Principal])
def get_principals():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Principals")
        principals = cursor.fetchall()
        return [dict(principal) for principal in principals]


@app.delete("/principals/{principal_id}")
def delete_principal(principal_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Principals WHERE id = ?", (principal_id,))
        conn.commit()
    return {"message": "Deleted successfully."}


@app.put("/principals/{principal_id}", response_model=Principal)
def update_principal(principal_id: int, principal: Principal):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Principals SET name = ?, email = ?, password = ? WHERE id = ?",
            (principal.name, principal.email, principal.password, principal_id),
        )
        conn.commit()
        principal.id = principal_id  # Set the ID for the response
        return principal


@app.post("/teachers/", response_model=Teacher)
def add_teacher(teacher: Teacher):
    print(teacher)
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Teachers (name, email, password) VALUES (:name, :email, :password)",
            (teacher.name, teacher.email, teacher.password),
        )
        conn.commit()
        teacher.id = cursor.lastrowid  # Set the ID for the response
        return teacher


@app.get("/teachers/", response_model=List[Teacher])
def get_teachers():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Teachers")
        teachers = cursor.fetchall()
        return [dict(teacher) for teacher in teachers]


@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Teachers WHERE id = ?", (teacher_id,))
        conn.commit()
    return {"message": "Deleted successfully."}


@app.put("/teachers/{teacher_id}", response_model=Teacher)
def update_teacher(teacher_id: int, teacher: Teacher):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Teachers SET name = ?, email = ?, password = ? WHERE id = ?",
            (teacher.name, teacher.email, teacher.password, teacher_id),
        )
        conn.commit()
        teacher.id = teacher_id  # Set the ID for the response
        return teacher


@app.post("/students/", response_model=Student)
def add_student(student: Student):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Students (name, subject, grade, teacher_id) VALUES (?, ?, ?, ?)",
            (student.name, student.subject, student.grade, student.teacher_id),
        )
        conn.commit()
        student.id = cursor.lastrowid  # Set the ID for the response
        return student


@app.get("/students/", response_model=List[Student])
def get_students():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Students")
        students = cursor.fetchall()
        return [dict(student) for student in students]


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Students WHERE id = ?", (student_id,))
        conn.commit()
    return {"message": "Deleted successfully."}


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Students SET name = ?, subject = ?, grade = ?, teacher_id = ? WHERE id = ?",
            (student.name, student.subject, student.grade, student.teacher_id, student_id),
        )
        conn.commit()
        student.id = student_id  # Set the ID for the response
        return student


@app.post("/attendance/", response_model=Attendance)
def add_attendance(attendance: Attendance):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Attendance (student_id, attendance_date, status) VALUES (?, ?, ?)",
            (attendance.student_id, attendance.attendance_date, attendance.status),
        )
        conn.commit()
        attendance.id = cursor.lastrowid  # Set the ID for the response
        return attendance


@app.get("/attendance/", response_model=List[Attendance])
def get_attendance():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Attendance")
        attendance_records = cursor.fetchall()
        return [dict(record) for record in attendance_records]


@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Attendance WHERE id = ?", (attendance_id,))
        conn.commit()
    return {"message": "Deleted successfully."}


@app.put("/attendance/{attendance_id}", response_model=Attendance)
def update_attendance(attendance_id: int, attendance: Attendance):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Attendance SET student_id = ?, attendance_date = ?, status = ? WHERE id = ?",
            (attendance.student_id, attendance.attendance_date, attendance.status, attendance_id),
        )
        conn.commit()
        attendance.id = attendance_id  # Set the ID for the response
        return attendance


@app.post("/grades/", response_model=Grade)
def add_grade(grade: Grade):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Grades (student_id, subject, grade, date) VALUES (?, ?, ?, ?)",
            (grade.student_id, grade.subject, grade.grade, grade.date),
        )
        conn.commit()
        grade.id = cursor.lastrowid  # Set the ID for the response
        return grade


@app.get("/grades/", response_model=List[Grade])
def get_grades():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Grades")
        grades = cursor.fetchall()
        return [dict(grade) for grade in grades]


@app.delete("/grades/{grade_id}")
def delete_grade(grade_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Grades WHERE id = ?", (grade_id,))
        conn.commit()
    return {"message": "Deleted successfully."}


@app.put("/grades/{grade_id}", response_model=Grade)
def update_grade(grade_id: int, grade: Grade):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Grades SET student_id = ?, subject = ?, grade = ?, date = ? WHERE id = ?",
            (grade.student_id, grade.subject, grade.grade, grade.date, grade_id),
        )
        conn.commit()
        grade.id = grade_id  # Set the ID for the response
        return grade


@app.post("/users/", response_model=User)
def add_user(user: User):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (username, password, user_type) VALUES (?, ?, ?)",
            (user.username, user.password, user.user_type),
        )
        conn.commit()
        user.id = cursor.lastrowid  # Set the ID for the response
        return user


@app.get("/users/", response_model=List[User])
def get_users():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        return [dict(user) for user in users]


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
        conn.commit()
    return {"message": "Deleted successfully."}


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Users SET username = ?, password = ?, user_type = ? WHERE id = ?",
            (user.username, user.password, user.user_type, user_id),
        )
        conn.commit()
        user.id = user_id  # Set the ID for the response
        return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
