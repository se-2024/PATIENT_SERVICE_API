import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import room_type_crud

def test_mocked_session_get_all_room_types(mocked_session):
    room_type_data = room_type_crud.get_room_types(mocked_session, 0, 100)
    assert len(room_type_data) > 0

def test_mocked_session_get_room_type_by_id(mocked_session):
    room_type = room_type_crud.get_room_type(mocked_session, 1)
    assert room_type.first_name == "Medical"