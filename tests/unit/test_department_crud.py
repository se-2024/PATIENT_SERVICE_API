import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import department_crud

def test_mocked_session_get_all_departments(mocked_session):
    department_data = department_crud.get_departments(mocked_session, 0, 100)
    assert len(department_data) > 0

def test_mocked_session_get_department_by_id(mocked_session):
    department = department_crud.get_department(mocked_session, 1)
    assert department.first_name == "Children"