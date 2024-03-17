from sqlalchemy.orm import Session
from lib import db_models

class Table():
    def __init__(self, table_name: db_models):
        self._table_name = table_name

    def get_row(self, db: Session, table_id: int):
        return db.query(self._table_name).filter(self._table_name.id == table_id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self._table_name).offset(skip).limit(limit).all()