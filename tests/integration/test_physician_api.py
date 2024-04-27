def test_physician_api(test_app):
    response = test_app.get("/physicians")
    assert response.status_code == 200
    assert response.json() == []