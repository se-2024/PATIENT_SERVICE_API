from sqlalchemy.orm import Session

from . import db_models


def get_hospital(db: Session, hopistal_id: int):
    return db.query(db_models.hospital).filter(db_models.hospital.id == hospital_id).first()

def get_hospitals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.hospital).offset(skip).limit(limit).all()
