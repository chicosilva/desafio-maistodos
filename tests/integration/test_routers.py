import pytest
import requests
from fastapi.testclient import TestClient

from app.main import application


@pytest.fixture
@pytest.mark.usefixtures("metadata_create_all")
def client(metadata_create_all):
    return TestClient(application)


def test_welcome_router(client):
    expected_response = "Welcome to the Doc Storage Api."
    response = client.get("/")

    assert response.status_code == 200
    assert expected_response in response.json()


def test_healthcheck_router(client):
    expected_response = {"status": "alive", "count": 0}
    response = client.get("/healthcheck")

    assert response.status_code == 200
    assert response.json() == expected_response


def test_get_person(requests_mock):

    url = "http://127.0.0.1:8000/person/list/"

    requests_mock.get(url, json={"success": True})
    assert {"success": True} == requests.get(url).json()
