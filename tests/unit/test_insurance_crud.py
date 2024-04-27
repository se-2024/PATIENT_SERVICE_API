import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import insurance_crud

def test_mocked_session_get_all_insurances(mocked_session):
    insurance_data = insurance_crud.get_insurances(mocked_session, 0, 100)
    assert len(insurance_data) > 0

def test_mocked_session_get_insurance_by_id(mocked_session):
    insurance = insurance_crud.get_insurance(mocked_session, 1)
    assert insurance.first_name == "Blueshield Cross"