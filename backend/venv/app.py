from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",  # Add your frontend origin here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
teachers_db = []
students_db = []
attendance_db = []
grades_db = []
users_db = {}

# Pydantic models
class Teacher(BaseModel):
    id: int
    name: str
    email: str

class Student(BaseModel):
    id: int
    name: str
    teacher_id: int

class Attendance(BaseModel):
    id: int
    student_id: int
    date: str
    status: str

class Grade(BaseModel):
    id: int
    student_id: int
    subject: str
    grade: str
    date: str

class User(BaseModel):
    username: str
    full_name: str
    role: str

class UserInDB(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Helper functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# User Authentication
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user['password']):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user['username'], "token_type": "bearer"}

@app.post("/signup", response_model=User)
async def signup(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = hash_password(user.password)
    user_in_db = UserInDB(**user.dict(), password=hashed_password)
    users_db[user.username] = user_in_db.dict()
    return user

# Teachers
@app.post("/teachers/", response_model=Teacher)
async def add_teacher(teacher: Teacher):
    if any(t.id == teacher.id for t in teachers_db):
        raise HTTPException(status_code=400, detail="Teacher with this ID already exists.")
    teachers_db.append(teacher)
    return teacher

@app.get("/teachers/", response_model=List[Teacher])
async def get_teachers():
    return teachers_db

# Students
@app.post("/students/", response_model=Student)
async def add_student(student: Student):
    if any(s.id == student.id for s in students_db):
        raise HTTPException(status_code=400, detail="Student with this ID already exists.")
    students_db.append(student)
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    return students_db

# Attendance
@app.post("/attendance/", response_model=Attendance)
async def add_attendance(attendance: Attendance):
    if any(a.id == attendance.id for a in attendance_db):
        raise HTTPException(status_code=400, detail="Attendance with this ID already exists.")
    attendance_db.append(attendance)
    return attendance

@app.get("/attendance/{student_id}", response_model=List[Attendance])
async def get_attendance(student_id: int):
    return [record for record in attendance_db if record.student_id == student_id]

# Grades
@app.post("/grades/", response_model=Grade)
async def add_grade(grade: Grade):
    if any(g.id == grade.id for g in grades_db):
        raise HTTPException(status_code=400, detail="Grade with this ID already exists.")
    grades_db.append(grade)
    return grade

@app.get("/grades/{student_id}", response_model=List[Grade])
async def get_grades(student_id: int):
    return [record for record in grades_db if record.student_id == student_id]

# Full report
@app.get("/full_report", response_model=Dict[str, List])
async def full_report():
    return {
        "teachers": teachers_db,
        "students": students_db,
        "attendance": attendance_db,
        "grades": grades_db,
    }

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
