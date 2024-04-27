def test_appointment_api(test_app):
    response = test_app.get("/appointments")
    assert response.status_code == 200
    assert response.json() == []