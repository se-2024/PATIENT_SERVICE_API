from sqlalchemy.orm import Session

from . import db_models


def get_medication(db: Session, medication_id: int):
    return db.query(db_models.Medication).filter(db_models.Medication.id == medication_id).first()

def get_medications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Medication).offset(skip).limit(limit).all()

