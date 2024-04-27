import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import employee_crud

def test_mocked_session_get_all_employees(mocked_session):
    employee_data = employee_crud.get_employees(mocked_session, 0, 100)
    assert len(employee_data) > 0

def test_mocked_session_get_employee_by_id(mocked_session):
    employee = employee_crud.get_employee(mocked_session, 1)
    assert employee.first_name == "Eric"