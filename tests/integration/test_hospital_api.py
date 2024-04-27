def test_hospital_api(test_app):
    response = test_app.get("/hospitals")
    assert response.status_code == 200
    assert response.json() == []