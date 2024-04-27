def test_mediaction_api(test_app):
    response = test_app.get("/mediactions")
    assert response.status_code == 200
    assert response.json() == []