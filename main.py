#!/usr/bin/env python
""" This is the entrypoint to the Patient Service API.
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from lib import employee_crud, hospital_crud, patient_crud, physician_crud, department_crud, prescription_crud, medication_crud, insurance_crud
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
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    employees = hospital_crud.get_hospitals(db, skip=skip, limit=limit)
    return employees