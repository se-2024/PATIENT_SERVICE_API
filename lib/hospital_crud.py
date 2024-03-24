from sqlalchemy.orm import Session

from . import db_models


<<<<<<< HEAD
def get_hospital(db: Session, hospital_id: int):
    return db.query(db_models.Hospital).filter(db_models.Patient.id == hospital_id).first()
=======
def get_hospital(db: Session, hopistal_id: int):
    return db.query(db_models.Hospital).filter(db_models.Hospital.id == hopistal_id).first()
>>>>>>> upstream/main

def get_hospitals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Hospital).offset(skip).limit(limit).all()
