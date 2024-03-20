from sqlalchemy.orm import Session

from . import db_models


def get_room_type(db: Session, room_type_id: int):
    return db.query(db_models.Room_Type).filter(db_models.Room_Type.id == room_type_id).first()

def get_room_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Room_Type).offset(skip).limit(limit).all()