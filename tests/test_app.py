import pytest
from app import app

@pytest.fixture
def client():
    # Flask provides a test client for simulating HTTP requests
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Azure Pipeline!" in response.data
