from sqlalchemy.orm import Session

from . import db_models


def get_appointment(db: Session, appointment_id: int):
    return db.query(db_models.Physician).filter(db_models.Appointment.id == appointment_id).first()

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Appointment).offset(skip).limit(limit).all()
