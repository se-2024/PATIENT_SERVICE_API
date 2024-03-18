from sqlalchemy.orm import Session

from . import db_models


def get_prescription(db: Session, prescription_id: int):
    return db.query(db_models.Prescription).filter(db_models.Prescription.id == prescription_id).first()

def get_prescriptions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Prescription).offset(skip).limit(limit).all()