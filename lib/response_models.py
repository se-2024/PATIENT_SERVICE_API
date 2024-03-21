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

<<<<<<< HEAD
class EmployeeBase(BaseModel):
    id: int
=======
class Department(BaseModel):
    id: int
    name: str
    hospital_id: int

class Medication(BaseModel):
    id: int
    name: str
    brand: str
    description: str
    
    
    class Config:
        orm_mode = True
        
class Employee(BaseModel):
>>>>>>> upstream/main
    first_name: str
    last_name: str
    ssn: str
    position: str
    hospital_id: int
    department_id: int

class Physician(Employee):
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

<<<<<<< HEAD
class Prescription(BaseModel):
    id: int
    patient_id: int
    prescribing_physcian_id: int
    medication_id: int    
    prescription_date: datetime.date
    quantity: str
    dosage: str
    frequency: str
    start_date: datetime.date
    end_date: datetime.date
    refill_available: int    

class Appointment(BaseModel):
    id: int
    patient_id: int
    physician_id: int
    appointment_date: datetime.date
    description: str

class Department(BaseModel):
    id: int
    name: str
    hospital_id: int    

class NurseBase(BaseModel):
    id: int
    qualification: str
=======
    class Config:
        orm_mode = True
>>>>>>> upstream/main

class Hospital(BaseModel):
    id: int
    name: str
<<<<<<< HEAD
    address: str      

class Manager(BaseModel):
    id: int     

    class Config:
        orm_mode = True 

class Medication(BaseModel):
    id: int
    name: str
    band: str 
    description: str       

class Insurance(BaseModel):
    id: int
    patinet_id: int
    provider_name: str
    policy_number: int 

class Room(BaseModel):
    id: int
    room_type_id: int
    available: str

class Room_Type(BaseModel):
    id: int
    type: str          

            



=======
    address: str
>>>>>>> upstream/main

    # This Config class is used to provide configurations to Pydantic.
    # https://docs.pydantic.dev/latest/api/config/
    # Pydantic's orm_mode will tell the Pydantic model to read the data 
    # even if it is not a dict, but an ORM model (or any other arbitrary object with attributes)
    # i.e. id = data["id"] or id = data.id
    class Config:
        orm_mode = True



class Prescription(BaseModel):
    id: int
    patient_id: int
    prescribing_physician_id: int
    medication_id: int
    prescription_date: datetime.date
    quantity: int
    dosage: str
    frequency: str
    start_date: datetime.date
    end_date: datetime.date
    refills_available: int

    class Config:
        orm_mode = True
        
        
class Insurance (BaseModel):
    id: int
    provider_name: str
    policy_number: str
    patient_id: int
