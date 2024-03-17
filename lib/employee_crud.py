from sqlalchemy.orm import Session

from . import db_models


def get_employee(db: Session, employee_id: int):
    return db.query(db_models.Employee).filter(db_models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Employee).offset(skip).limit(limit).all()