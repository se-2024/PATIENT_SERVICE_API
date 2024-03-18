#!/usr/bin/env python
""" Responsible for the pydantic API models
Create Pydantic models (schemas) that will be used when reading data
and returning it from the API to the user.
Pydantic also uses the term "model" to refer to something different
than the database models. It provides the data validation and conversion
classes and instances.
"""
import datetime
from pydantic import BaseModel

# Note:
# Pydantic models declare the types using :,
# the new type annotation syntax/type hints:
# i.e name: str

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    ssn: str
    position: str
    hospital_id: int
    department_id: int

class Physician(EmployeeBase):
    id: int
    specialty: str

    class Config:
        orm_mode = True

class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: datetime.date
    ssn: str
    gender: str
    address: str
    physician_id: int

    # This Config class is used to provide configurations to Pydantic.
    # https://docs.pydantic.dev/latest/api/config/
    # Pydantic's orm_mode will tell the Pydantic model to read the data 
    # even if it is not a dict, but an ORM model (or any other arbitrary object with attributes)
    # i.e. id = data["id"] or id = data.id
    class Config:
        orm_mode = True

class AppointmentBase(BaseModel):
    patient_id: int
    physician_id: int
    appointment_date: date
    description: Optional[str] = None

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True

class Hospital(BaseModel):
    id: int
    name: str
    address: str

    class Config:
        orm_mode = True

class Insurance(BaseModel):
    id: int
    patient_id: int
    provider_name: str
    policy_number: str

    class Config:
        orm_mode = True

class Manager(BaseModel):
    id: int
    employee_id: int

    class Config:
        orm_mode = True

class Medication(BaseModel):
    id: int
    name: str
    brand: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class Nurse(EmployeeBase):
    id: int

    class Config:
        orm_mode = True

class Prescription(BaseModel):
    id: int
    patient_id: int
    prescribing_physician_id: int
    medication_id: int
    prescription_date: date
    quantity: int
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    refills_available: int = 0

    class Config:
        orm_mode = True

class Room(BaseModel):
    id: int
    room_type_id: int
    available: bool

    class Config:
        orm_mode = True

class RoomType(BaseModel):
    id: int
    type: str

    class Config:
        orm_mode = True