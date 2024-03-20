from sqlalchemy.orm import Session

from . import db_models


def get_hospital(db: Session, hopistal_id: int):
    return db.query(db_models.Hospital).filter(db_models.Hospital.id == hopistal_id).first()

def get_hospitals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Hospital).offset(skip).limit(limit).all()
