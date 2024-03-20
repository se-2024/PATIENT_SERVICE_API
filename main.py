#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from lib import patient_crud, physician_crud, employee_crud, department_crud, hospital_crud, manager_crud, medication_crud, insurance_crud, nurse_crud, room_crud, room_type_crud, prescription_crud, appointment_crud
from lib import response_models
from lib.database_connection import SessionLocal

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

@app.get("/patients/", response_model=List[response_models.Patient])
def get_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = patient_crud.get_patients(db, skip=skip, limit=limit)
    return patients

@app.get("/physicians/", response_model=List[response_models.Physician])
def get_physicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    physicians = physician_crud.get_physicians(db, skip=skip, limit=limit)
    return physicians

@app.get("/employees/", response_model=List[response_models.Employee])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = employee_crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/department/", response_model=List[response_models.Department])
def get_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_departments = department_crud.get_departments(db, skip=skip, limit=limit)
    return get_departments

@app.get("/hospital/", response_model=List[response_models.Hospital])
def get_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_hospitals = hospital_crud.get_hospitals(db, skip=skip, limit=limit)
    return get_hospitals

@app.get("/manager/", response_model=List[response_models.Manager])
def get_managers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_managers = manager_crud.get_managers(db, skip=skip, limit=limit)
    return get_managers

@app.get("/insurance/", response_model=List[response_models.Insurance])
def get_insurances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_insurances = insurance_crud.get_insurances(db, skip=skip, limit=limit)
    return get_insurances

@app.get("/nurse/", response_model=List[response_models.Nurse])
def get_nurses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_nurses = nurse_crud.get_nurses(db, skip=skip, limit=limit)
    return get_nurses

@app.get("/room/", response_model=List[response_models.Room])
def get_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_rooms = room_crud.get_rooms(db, skip=skip, limit=limit)
    return get_rooms

@app.get("/room_type/", response_model=List[response_models.Room_Type])
def get_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_room_types = room_type_crud.get_room_types(db, skip=skip, limit=limit)
    return get_room_types

@app.get("/prescription/", response_model=List[response_models.Prescription])
def get_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_prescriptions = room_crud.get_prescriptions(db, skip=skip, limit=limit)
    return get_prescriptions

@app.get("/appointment/", response_model=List[response_models.Appointment])
def get_appoitments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_appointments = room_crud.get_appointments(db, skip=skip, limit=limit)
    return get_appoitments

@app.get("/medication/", response_model=List[response_models.Medication])
def get_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_mendications = room_crud.get_medications(db, skip=skip, limit=limit)
    return get_medications

