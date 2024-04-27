def test_department_api(test_app):
    response = test_app.get("/departments")
    assert response.status_code == 200
    assert response.json() == []