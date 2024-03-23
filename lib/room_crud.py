from sqlalchemy.orm import Session

from . import db_models


def get_room(db: Session, room_id: int):
    return db.query(db_models.Room).filter(db_models.Room.id == room_id).first()

def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_models.Room).offset(skip).limit(limit).all()