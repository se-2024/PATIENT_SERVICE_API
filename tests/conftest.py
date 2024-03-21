import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

import pytest
from datetime import datetime
from starlette.testclient import TestClient
# needed for database testing
from lib.database_connection import Base
# needed for api testing
from main import app

@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base

@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    return [("patient", [
        {
            "id": 1,
            "first_name": "Kevin",
            "last_name": "James",
            "dob": datetime.strptime("1976-02-13", "%Y-%m-%d"),
            "ssn": "123456789",
            "gender": "male",
            "address": "123 Comedy Lane"
        }
    ])]

@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here