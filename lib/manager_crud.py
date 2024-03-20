from sqlalchemy.orm import Session

from . import db_models


def get_manager(db: Session, manager_id: int):
    return db.query(db_models.Manager).filter(db_models.Manager.id == manager_id).first()

def get_managers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Manager).offset(skip).limit(limit).all()