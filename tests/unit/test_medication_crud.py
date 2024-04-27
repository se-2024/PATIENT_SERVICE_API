import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import medication_crud

def test_mocked_session_get_all_medications(mocked_session):
    medication_data = medication_crud.get_medications(mocked_session, 0, 100)
    assert len(medication_data) > 0

def test_mocked_session_get_medication_by_id(mocked_session):
    medication = medication_crud.get_medication(mocked_session, 1)
    assert medication.first_name == "Antibiotics"