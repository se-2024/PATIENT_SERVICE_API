#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from lib import (
    employee_crud, 
    hospital_crud,
    patient_crud, 
    physician_crud, 
    department_crud, 
    prescription_crud, 
    medication_crud, 
    insurance_crud, 
    nurse_crud, 
    room_crud, 
    appointment_crud, 
    manager_crud, 
    room_type_crud,
    response_models,
)

from lib.database_connection import SessionLocal
from lib.middleware.exception_handler import CORSMiddleware

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

# Sample list of patients
patients = [
    {
        "id": 95810900,
        "first_name": "aliquip amet",
        "last_name": "Lorem quis mollit ut",
        "dob": "laboris nostrud in nisi",
        "ssn": "deserunt minim commodo",
        "gender": "est dolore",
        "address": "fugiat aliquip ea",
        "physician_id": 82655953,
    },
    {
        "id": 74048341,
        "first_name": "anim voluptate do velit",
        "last_name": "id deserunt magna dolor reprehenderit",
        "dob": "sit sint laboris",
        "ssn": "consequat",
        "gender": "aliquip",
        "address": "magna in",
        "physician_id": 46100215,
    },
    {
        "id": 53286456,
        "first_name": "pariatur nisi sunt aute eu",
        "last_name": "labore quis mollit ea",
        "dob": "consequat aliquip esse irure",
        "ssn": "ipsum et cillum proident",
        "gender": "commodo sunt in",
        "address": "eiusmod nostrud",
        "physician_id": 85103142,
    },
]

@app.get("/patients")
async def get_patients(
    skip: int = 0,
    limit: int = 100,
    sort: str = "desc",
    sort_column: str = None,
    db: Session = Depends(get_db),  # Assuming get_db is defined somewhere else
):
    return patients


@app.get("/physicians/", response_model=List[response_models.Physician])
def get_physicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    physicians = physician_crud.get_physicians(db, skip=skip, limit=limit)
    return physicians

@app.get("/departments/", response_model=List[response_models.Department])
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = department_crud.get_departments(db, skip=skip, limit=limit)
    return departments

@app.get("/prescriptions/", response_model=List[response_models.Prescription])
def get_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prescriptions = prescription_crud.get_prescriptions(db, skip=skip, limit=limit)
    return prescriptions

@app.get("/medications/", response_model=List[response_models.Medication])
def get_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = medication_crud.get_medications(db, skip=skip, limit=limit)
    return medications

@app.get("/insurances/", response_model=List[response_models.Insurance])
def get_insurance(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    insurances = insurance_crud.get_insurance(db, skip=skip, limit=limit)
    return insurances

@app.get("/employees/", response_model=List[response_models.Employee])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = employee_crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/hospitals/", response_model=List[response_models.Hospital])
def get_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hospitals = hospital_crud.get_hospitals(db, skip=skip, limit=limit)
    return hospitals

@app.get("/nurses/", response_model=List[response_models.Nurse])
def get_nurses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nurses = nurse_crud.get_nurses(db, skip=skip, limit=limit)
    return nurses

@app.get("/rooms/", response_model=List[response_models.Room])
def get_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms =room_crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get("/managers/", response_model=List[response_models.Manager])
def get_managers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    managers =manager_crud.get_manager(db, skip=skip, limit=limit)
    return managers

@app.get("/appointments/", response_model=List[response_models.Appointment])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments =appointment_crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@app.get("/room_types/", response_model=List[response_models.Room_Type])
def get_room_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    room_types =room_type_crud.get_room_types(db, skip=skip, limit=limit)
    return room_types
