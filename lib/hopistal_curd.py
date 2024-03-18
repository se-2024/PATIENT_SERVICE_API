from sqlalchemy.orm import Session

from . import db_models


def get_hopistal(db: Session, hopistal_id: int):
    return db.query(db_models.hopistal).filter(db_models.hopistal.id == hopistal_id).first()

def get_hopistals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.hopistal).offset(skip).limit(limit).all()
