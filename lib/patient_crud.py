# -*- coding: utf-8 -*-
from fastapi import HTTPException
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from . import db_models


def get_patient(db: Session, patient_id: int):
    return db.query(db_models.Patient).filter(db_models.Patient.id == patient_id).first()


def get_patients(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    sort: str = None,
    sort_column=None,
):
    if sort is not None and sort_column is not None:
        valid_sort_options = ["desc", "asc"]
        if sort not in valid_sort_options:
            message = f"""
                Invalid sort option - cannot sort {sort}:
                Valid options are {','.join(valid_sort_options)}
                """

            raise HTTPException(
                status_code=400,
                detail=message,
            )
        # Dynamically get the column to sort by.
        sort_by = getattr(db_models.Patient, sort_column, None)
        if sort_by is None:
            # Raise HTTP exception with a 400 status code
            # and a clear error message.
            raise HTTPException(status_code=400, detail=f"Invalid sort column: {sort_column}")

        # Apply sort order.
        if sort == "asc":
            query_order_by = asc(sort_by)
        else:
            query_order_by = desc(sort_by)
        return db.query(db_models.Patient).order_by(query_order_by).offset(skip).limit(limit).all()
    return db.query(db_models.Patient).offset(skip).limit(limit).all()
