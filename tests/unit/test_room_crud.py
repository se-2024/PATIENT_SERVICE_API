import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from lib import room_crud

def test_mocked_session_get_all_rooms(mocked_session):
    room_data = room_crud.get_rooms(mocked_session, 0, 100)
    assert len(room_data) > 0

def test_mocked_session_get_room_by_id(mocked_session):
    room = room_crud.get_room(mocked_session, 1)
    assert room.first_name == "ER"