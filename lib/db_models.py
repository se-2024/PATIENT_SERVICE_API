
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

# Represents a nurse providing medical care and assistance within the healthcare system.
class Nurse(Base):
    __tablename__ = "nurse"
    id = Column(Integer, primary_key=True)
    qualification = Column(String)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship("Employee", back_populates="nurse")

# Represents a healthcare facility where medical services are provided.
class Hospital(Base):
    __tablename__ = "hospital"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    departments = relationship("Department", back_populates="hospital")
    employees = relationship("Employee", back_populates="hospital")

# Represents a general employee within the healthcare system, including nurses, physicians, and managers.
class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    SSN = Column(String(9), nullable=False)
    position = Column(String)
    hospital_id = Column(Integer, ForeignKey('hospital.id'), nullable=False)
    hospital = relationship("Hospital", back_populates="employees")
    department = relationship("Department", back_populates="employees")

# Represents a department within a hospital, organizing employees and resources for specific functions.
class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hospital_id = Column(Integer, ForeignKey('hospital.id'), nullable=False)
    hospital = relationship("Hospital", back_populates="departments")
    employees = relationship("Employees", back_populates="department")

# Represents a manager overseeing operations within a department or healthcare facility.
class Manager(Base):
    __tablename__ = "manager"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), unique=True)
    employee = relationship("Employee", back_populates="manager")

# Represents an insurance policy associated with a patient.
class Insurance(Base):
    __tablename__ = "insurance"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
    provider_name = Column(String(255), nullable=False)
    policy_number = Column(String(255), nullable=False)
    patient = relationship("Patient", back_populates="insurance")

# Represents a scheduled appointment between a patient and a physician.
class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
    physician_id = Column(Integer, ForeignKey('physician.id'), nullable=False)
    appointment_date = Column(TIMESTAMP, nullable=False)
    description = Column(Text)
    patient = relationship("Patient", back_populates="appointments")
    physician = relationship("Physician", back_populates="appointments")

#  Represents a prescribed medication for a patient, including dosage and refills.
class Prescription(Base):
    __tablename__ = "prescription"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=False)
    prescribing_physician_id = Column(Integer, ForeignKey('physician.id'), nullable=False)
    medication_id = Column(Integer, ForeignKey('medication.id'), nullable=False)
    prescription_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    dosage = Column(Text)
    frequency = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    refills_available = Column(Integer, nullable=False, default=0)

    patient = relationship("Patient", back_populates="prescriptions")
    prescribing_physician = relationship("Physician", back_populates="prescriptions")
    medication = relationship("Medication", back_populates="prescriptions")

# Medication
class Medication(Base):
    __tablename__ = "medication"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    brand = Column(Text, nullable=False)
    description = Column(Text)

    prescriptions = relationship("Prescription", back_populates="medication")

#  Represents different types of rooms available in a healthcare facility.
class Room_Type(Base):
    __tablename__ = "room_type"
    id = Column(Integer, primary_key=True)
    type = Column(String(25), nullable=False)

#  Represents individual rooms within a healthcare facility.
class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    room_type_id = Column(Integer, ForeignKey('room_type.id'), nullable=False)
    available = Column(Boolean, nullable=False, default=True) 