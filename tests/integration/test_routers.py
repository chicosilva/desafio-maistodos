from datetime import date
import pytest
import requests
from fastapi.testclient import TestClient

from app.main import application

@pytest.fixture
@pytest.mark.usefixtures('metadata_create_all')
def client(metadata_create_all):
    return TestClient(application)

def test_welcome_router(client):
    expected_response = 'Welcome to the MaisTodos.'
    response = client.get('/')

    assert response.status_code == 200
    assert expected_response in response.json()

def test_healthcheck_router(client):
    expected_response = {'status': 'alive', 'count': 0}
    response = client.get('/healthcheck')

    assert response.status_code == 200
    assert response.json() == expected_response

def test_get_cards(requests_mock):

    url = 'http://127.0.0.1:8000/api/v1/credit-card/'

    requests_mock.get(url, json={'success': True})
    assert {'success': True} == requests.get(url).json()

def test_create_card(client, token):
    response = client.post(
        '/api/v1/credit-card/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'exp_date': '02/2026',
            'holder': 'Francisco A silva',
            'number': '4539578763621486',
            'cvv': '123'
        },
    )
    assert response.status_code == 201
    assert response.json()['holder'] == 'Francisco A silva'
    assert response.json()['exp_date'] == '2026-02-28'
    assert response.json()['number'] == '4539578763621486'
    assert response.json()['cvv'] == 123
