from copy import deepcopy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module

@pytest.fixture
def client():
    with TestClient(app_module.app) as c:
        yield c

@pytest.fixture(autouse=True)
def snapshot_activities():
    snapshot = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(snapshot)
