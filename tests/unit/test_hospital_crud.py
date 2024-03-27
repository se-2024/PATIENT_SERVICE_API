import sys, os

from lib.db_models import Hospital
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import hospital_crud

def test_mocked_session_get_all_hospitals(mocked_session: hospital_crud.Session):
    hospital_data = hospital_crud.get_hospitals(mocked_session, 0, 100)
    assert len(hospital_data) >= 0

def test_mocked_session_get_hosptital_by_id(mocked_session: hospital_crud.Session):
    hospital = hospital_crud.get_hospitals(mocked_session, 1)
    assert Hospital.name == "New York"