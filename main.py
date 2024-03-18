#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from lib import patient_crud, physician_crud
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

@app.get("/appointments/", response_model=List[response_models.Appointment])
def get_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = appointment_crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@app.get("/employees/", response_model=List[response_models.EmployeeBase])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = employee_crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/hospitals/", response_model=List[response_models.Hospital])
def get_hospitals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    hospitals = hospital_crud.get_hospitals(db, skip=skip, limit=limit)
    return hospitals

@app.get("/insurances/", response_model=List[response_models.Insurance])
def get_insurances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    insurances = insurance_crud.get_insurances(db, skip=skip, limit=limit)
    return insurances

@app.get("/managers/", response_model=List[response_models.Manager])
def get_managers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    managers = manager_crud.get_managers(db, skip=skip, limit=limit)
    return managers

@app.get("/medications/", response_model=List[response_models.Medication])
def get_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = medication_crud.get_medications(db, skip=skip, limit=limit)
    return medications

@app.get("/nurses/", response_model=List[response_models.Nurse])
def get_nurses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nurses = nurse_crud.get_nurses(db, skip=skip, limit=limit)
    return nurses

@app.get("/prescriptions/", response_model=List[response_models.Prescription])
def get_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prescriptions = prescription_crud.get_prescriptions(db, skip=skip, limit=limit)
    return prescriptions

@app.get("/rooms/", response_model=List[response_models.Room])
def get_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = room_crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get("/room_types/", response_model=List[response_models.RoomType])
def get_room_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    room_types = room_type_crud.get_room_types(db, skip=skip, limit=limit)
    return room_types
