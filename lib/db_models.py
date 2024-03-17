
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
    insurances = relationship('Insurance', backref='patient')

class Insurance(Base):
    __tablename__="insurance"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    provider_name = Column(String,nullable=False)
    policy_number = Column(String,nullable=False)
    
    
