import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import prescription_crud

def test_mocked_session_get_all_prescriptions(mocked_session):
    prescription_data = prescription_crud.get_prescriptions(mocked_session, 0, 100)
    assert len(prescription_data) > 0

def test_mocked_session_get_prescriptions_by_id(mocked_session):
    prescription = prescription_crud.get_patient(mocked_session, 1)
    assert prescription.first_name == "Asprin"