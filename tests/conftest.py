import importlib
import os
import sys

import pytest
from starlette.testclient import TestClient

from lib.database_connection import Base
from main import app
from tests.helpers.fake_table_loader import FakeTableLoader

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))


# needed for database testing

# needed for api testing


def find_data_by_key(data, key):
    for item in data:
        if item[0] == key:
            return item[1]  # Return the data associated with the key
    return None  # Return None if no matching key is found


def merge_back_to_data(data, key, new_data):
    for index, (current_key, value) in enumerate(data):
        if current_key == key:
            data[index] = (key, new_data)  # Replace the old tuple with the new one
            break
    return data


def add_test_data(entities):

    working_dir = os.path.dirname(os.path.abspath(__file__))
    directory = f"{working_dir}/fixtures"

    # Walk through the directory
    for _, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".py"):
                entity = filename.replace(".py", "")
                module = importlib.import_module(f"tests.fixtures.{entity}")
                test_data = getattr(module, entity)
                entity_data = find_data_by_key(entities, entity)
                modified_data = [*entity_data, *test_data]
                # Merge the modified entity data back into the original data list
                updated_data = merge_back_to_data(entities, entity, modified_data)
    return updated_data


@pytest.fixture(scope="function")
def sqlalchemy_declarative_base():
    return Base


@pytest.fixture(scope="function")
def sqlalchemy_mock_config():
    loader = FakeTableLoader()
    entities = loader.load()

    return add_test_data(entities)


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
