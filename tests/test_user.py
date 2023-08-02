"""
    Here is my pytest test file.
    Poetry manages my environment, so pytest runs smoothly.
"""

import pytest
from fastapi.testclient import TestClient
from awesome_fastapi_project.user.routers import router

@pytest.fixture
def client():
    client = TestClient(router)
    return client

def test_get_users(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World! Are you lost? This is not the page you're looking for."}

def test_create_user(client):
    response = client.post("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World! You just created a user. Congratulations, you're now a parent!"}

def test_get_user(client):
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World! You're looking for user 1? Sorry, they're on vacation in Hawaii."}

def test_update_user(client):
    response = client.put("/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World! User 1 has been updated. They now have a new hat."}

def test_delete_user(client):
    response = client.delete("/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World! User 1 has been deleted. Don't worry, they'll be back in the sequel."}