def test_manager_api(test_app):
    response = test_app.get("/managers")
    assert response.status_code == 200
    assert response.json() == []