def test_room_type_api(test_app):
    response = test_app.get("/room_types")
    assert response.status_code == 200
    assert response.json() == []