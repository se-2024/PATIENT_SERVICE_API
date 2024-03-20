
""" Responsible for creating the Database Models
# SQLAlchemy uses the term "model" to refer to these classes 
# and instances that interact with the database.
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import mapped_column, relationship
from .database_connection import Base

# Note:
# SQLAlchemy models define attributes
# using =, and pass the type as a parameter to Column
# i.e name = Column(String)

class Physician(Base):
    __tablename__ = "physician"
    id = Column(Integer, primary_key=True)
    specialty = Column(String)
    patients = relationship('Patient', backref='physician')

class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    ssn = Column(String, nullable=False)
    gender = Column(String)
    address = Column(String)
    physician_id = Column(Integer, ForeignKey('physician.id'))

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))

class Prescription(Base):
    __tablename__ = "prescription"
    id = Column(Integer, primary_key=True)
    prescription_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable= False)
    dosage = Column(String)
    frequency = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    refills_available = Column(Integer, nullable=False, default = 0)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    medication_id = Column(Integer, ForeignKey('medication.id'))
    prescribing_physician_id = Column(Integer, ForeignKey('physician.id'))
    
class Medication(Base):
    __tablename__ = "medication"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    description = Column(String)
