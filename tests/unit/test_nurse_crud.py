import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import nurse_crud

def test_mocked_session_get_all_nurses(mocked_session):
    nurse_data = nurse_crud.get_nurses(mocked_session, 0, 100)
    assert len(nurse_data) > 0

def test_mocked_session_get_nurse_by_id(mocked_session):
    nurse = nurse_crud.get_nurse(mocked_session, 1)
    assert nurse.first_name == "Tim"