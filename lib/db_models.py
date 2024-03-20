
""" Responsible for creating the Database Models
# SQLAlchemy uses the term "model" to refer to these classes 
# and instances that interact with the database.
"""
import datetime
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
    hospital_id = Column(Integer, primary_key=True)

class Hospital(Base):
     __tablename__ = "hospital"
     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False)
     address = Column(String)

class Room_Type(Base) :
      __tablename__ = "room_type"
      id = Column(Integer, primary_key=True)
      type = Column(String)

class Manager(Base) :
      __tablename__ = "manager"
      id = Column(Integer, primary_key=True)
    
class Insurance(Base) :
      __tablename__ = "insurance"
      id = Column(Integer, primary_key=True)
      patient_id = Column(Integer, primary_key=True)
      provider_name = Column(String)
      policy_number = Column(Integer, primary_key=True)

class Nurse(Base) :
      __tablename__ = "nurse"
      id = Column(Integer, primary_key=True)
      qualification = Column(String)

class Room(Base) :
     __tablename__ = "room"
     id = Column(Integer, primary_key=True)
     room_type_id = Column(Integer, primary_key=True)
     available = Column(Date)

class Prescription(Base):
     __tablename__ = "prescription"
     id = Column(Integer, primary_key=True)
     patient_id = Column(Integer, foreign_key=True)
     prescibing_physician_id = Column(Integer)
     medication_id = Column(Integer, foreign_key=True)
     prescription_date = Column(Date)
     quantity = Column(Integer)
     dosage = Column(Integer)
     frequency = Column(String)
     start_date = Column(Date)
     end_date =  Column(Date)
     refills_available = Column(Date)

class Medication(Base):
    __tablename__ = "medication"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    description = Column(String)
class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, foreign_key=True)
    prescibing_physician_id = Column(Integer)
    appointment_date = Column(Date)
    description = Column(String)

class EmployeeBase(Base):
    __tablename__ = "employee"
    id =  Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    ssn = Column(Integer)
    position = Column(String)
    hospital_id = Column(Integer, foreign_key=True)
    department_id = Column(Integer, foreign_key=True)