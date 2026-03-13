import pytest
from bottle import Bottle
from bapi import ninjas  # Import the ninjas list

@pytest.fixture
def app():
    # Create a test app instance
    from bapi import app
    return app

@pytest.fixture
def client(app):
    # Return a test client
    return app.test_client()

def test_get_ninjas(client):
    """Test the GET /api/ninjas endpoint"""
    response = client.get('/api/ninjas')
    assert response.status_code == 200
    data = response.json
    assert 'data' in data
    assert data['data'] == ninjas  # Assuming ninjas is the list from bapi.py
    assert len(data['data']) == 3  # Initial 3 ninjas

def test_post_ninja_success(client):
    """Test the POST /api/ninjas endpoint with valid data"""
    new_ninja = {
        "name": "Bullet",
        "belt_color": "black",
        "speciality": "Bullet Time"
    }
    response = client.post('/api/ninjas', json=new_ninja)
    assert response.status_code == 201
    data = response.json
    assert 'message' in data
    assert 'data' in data
    assert data['data'] == new_ninja

def test_post_ninja_invalid(client):
    """Test the POST /api/ninjas endpoint with invalid data"""
    response = client.post('/api/ninjas', json="invalid")
    assert response.status_code == 400

def test_home_route(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    # Since it's a template, we can check if it contains expected content
    content = response.body.decode('utf-8')
    assert 'Ninja Town' in content
    assert 'Welcome Ninja Town' in content
