from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Principal(Base):
    __tablename__ = 'Principals'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Teacher(Base):
    __tablename__ = 'Teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Student(Base):
    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    subject = Column(String, nullable=True)
    grade = Column(String, nullable=True)
    teacher_id = Column(Integer, nullable=True)

class Attendance(Base):
    __tablename__ = 'Attendance'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    attendance_date = Column(String)
    status = Column(String)

class Grade(Base):
    __tablename__ = 'Grades'
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    subject = Column(String)
    grade = Column(Float)
    date = Column(Date)

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    user_type = Column(String)
