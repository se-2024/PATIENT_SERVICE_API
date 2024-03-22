def test_patient_api(test_app):
    response = test_app.get("/patients")
    assert response.status_code == 200
    assert response.json() == []