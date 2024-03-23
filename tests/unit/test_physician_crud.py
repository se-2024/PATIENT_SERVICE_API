import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import physician_crud

def test_mocked_session_get_all_physicians(mocked_session):
    physician_data = physician_crud.get_physicians(mocked_session, 0, 100)
    assert len(physician_data) > 0

def test_mocked_session_get_physicians_by_id(mocked_session):
    physician = physician_crud.get_physcian(mocked_session, 1)
    assert physician.first_name == "Asprin"