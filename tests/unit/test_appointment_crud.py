import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import appointment_crud

def test_mocked_session_get_all_appointments(mocked_session):
    appointment_data = appointment_crud.get_appointments(mocked_session, 0, 100)
    assert len(appointment_data) > 0

def test_mocked_session_get_appointment_by_id(mocked_session):
    appointment = appointment_crud.get_appointment(mocked_session, 1)
    assert appointment.first_name == "eye appointment"