def test_nurse_api(test_app):
    response = test_app.get("/nurses")
    assert response.status_code == 200
    assert response.json() == []