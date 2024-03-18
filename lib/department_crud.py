from sqlalchemy.orm import Session

from . import db_models


def get_department(db: Session, department_id: int):
    return db.query(db_models.Department).filter(db_models.Department.id == department_id).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Department).offset(skip).limit(limit).all()

