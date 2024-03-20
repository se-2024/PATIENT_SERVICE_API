from sqlalchemy.orm import Session

from . import db_models


def get_nurse(db: Session, nurse_id: int):
    return db.query(db_models.Nurse).filter(db_models.Nurse.id == nurse_id).first()

def get_nurses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Nurse).offset(skip).limit(limit).all()