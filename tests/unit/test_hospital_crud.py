import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import hospital_crud

def test_mocked_session_get_all_hospitals(mocked_session):
    hospital_data = hospital_crud.get_hospitals(mocked_session, 0, 100)
    assert len(hospital_data) > 0

def test_mocked_session_get_hospital_by_id(mocked_session):
    hospital = hospital_crud.get_hospital(mocked_session, 1)
    assert hospital.first_name == "Parkland"