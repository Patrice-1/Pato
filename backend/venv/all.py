from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from .database import get_db
from .models import Principal, Teacher, Student, Attendance, Grade, User, Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models (for request/response validation)
class PrincipalCreate(BaseModel):
    name: str
    email: str
    password: str

class PrincipalResponse(PrincipalCreate):
    id: int

# Add similar classes for Teacher, Student, Attendance, Grade, User

@app.post("/principals/", response_model=PrincipalResponse)
def add_principal(principal: PrincipalCreate, db: Session = Depends(get_db)):
    db_principal = Principal(**principal.dict())
    db.add(db_principal)
    db.commit()
    db.refresh(db_principal)
    return db_principal

@app.get("/principals/", response_model=List[PrincipalResponse])
def get_principals(db: Session = Depends(get_db)):
    return db.query(Principal).all()

@app.delete("/principals/{principal_id}")
def delete_principal(principal_id: int, db: Session = Depends(get_db)):
    db_principal = db.query(Principal).filter(Principal.id == principal_id).first()
    if db_principal is None:
        raise HTTPException(status_code=404, detail="Principal not found")
    db.delete(db_principal)
    db.commit()
    return {"message": "Deleted successfully."}

@app.put("/principals/{principal_id}", response_model=PrincipalResponse)
def update_principal(principal_id: int, principal: PrincipalCreate, db: Session = Depends(get_db)):
    db_principal = db.query(Principal).filter(Principal.id == principal_id).first()
    if db_principal is None:
        raise HTTPException(status_code=404, detail="Principal not found")
    for key, value in principal.dict().items():
        setattr(db_principal, key, value)
    db.commit()
    db.refresh(db_principal)
    return db_principal

# Repeat similar changes for Teacher, Student, Attendance, Grade, User routes

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
