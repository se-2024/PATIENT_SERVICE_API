import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import hospital_crud

def test_mocked_session_get_all_hospitals(mocked_session: hospital_crud.Session):
    patient_data = hospital_crud.get_patients(mocked_session, 0, 100)
    assert len(patient_data) > 0

def test_mocked_session_get_patient_by_id(mocked_session: hospital_crud.Session):
    hospital = hospital_crud.get_patient(mocked_session, 1)
    assert hospital.first_name == "Kevin"