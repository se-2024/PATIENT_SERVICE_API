from sqlalchemy.orm import Session

from . import db_models


def get_insurance(db: Session, insurance_id: int):
    return db.query(db_models.Insurance).filter(db_models.Insurance.id == insurance_id).first()

def get_insurance(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Insurance).offset(skip).limit(limit).all()

