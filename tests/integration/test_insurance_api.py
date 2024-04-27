def test_insurance_api(test_app):
    response = test_app.get("/insurances")
    assert response.status_code == 200
    assert response.json() == []