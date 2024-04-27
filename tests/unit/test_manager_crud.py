import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import manager_crud

def test_mocked_session_get_all_managers(mocked_session):
    manager_data = manager_crud.get_managers(mocked_session, 0, 100)
    assert len(manager_data) > 0

def test_mocked_session_get_manager_by_id(mocked_session):
    manager = manager_crud.get_manager(mocked_session, 1)
    assert manager.first_name == "Steve"