import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import patient_crud

def test_mocked_session_get_all_patients(mocked_session):
    patient_data = patient_crud.get_patients(mocked_session, 0, 100)
    assert len(patient_data) > 0

def test_mocked_session_get_patient_by_id(mocked_session):
    patient = patient_crud.get_patient(mocked_session, 1)
    assert patient.first_name == "Kevin"