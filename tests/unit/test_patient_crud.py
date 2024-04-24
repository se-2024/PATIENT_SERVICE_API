# -*- coding: utf-8 -*-
import os
import sys

from lib import patient_crud

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))


def test_mocked_session_get_all_patients(mocked_session):
    patient_data = patient_crud.get_patients(mocked_session, 0, 100)
    assert len(patient_data) > 0


def test_mocked_session_get_all_patients_sort_desc(mocked_session):
    patient_data = patient_crud.get_patients(mocked_session, 0, 100, "desc", sort_column="id")
    assert len(patient_data) > 0
    assert patient_data[0].id == 9999999


def test_mocked_session_get_all_patients_sort_asc(mocked_session):
    patient_data = patient_crud.get_patients(mocked_session, 0, 100)
    assert len(patient_data) > 0
    assert patient_data[0].id == 1


def test_mocked_session_get_patient_by_id(mocked_session):
    patient = patient_crud.get_patient(mocked_session, 1)
    assert patient.first_name == "Michael"
