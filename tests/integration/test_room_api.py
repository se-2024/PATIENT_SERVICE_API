def test_room_api(test_app):
    response = test_app.get("/rooms")
    assert response.status_code == 200
    assert response.json() == []