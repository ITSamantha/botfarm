import uuid
import pytest
from fastapi.testclient import TestClient
from src.main import get_application
from http import HTTPStatus


@pytest.fixture
def client():
    app = get_application()
    with TestClient(app) as client:
        yield client


def test_create_user(client):
    user_data = {
        "autogenerate": False,
        "data": {
            "login": "test@example.com",
            "password": "securepassword",
            "project_id": uuid.uuid4(),
            "env_id": 1,
            "domain_id": 1,
        },
    }

    response = client.post("/users", json=user_data)
    assert response.status_code == HTTPStatus.OK
    user_json = response.json()
    assert "id" in user_json
    assert user_json["login"] == "test@example.com"


def test_get_user_by_id(client):
    user_data = {
        "autogenerate": False,
        "data": {
            "login": "test2@example.com",
            "password": "anothersecurepassword",
            "project_id": uuid.uuid4(),
            "env_id": 1,
            "domain_id": 1,
        },
    }
    create_response = client.post("/users", json=user_data)
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["login"] == "test2@example.com"


def test_delete_user(client):
    user_data = {
        "autogenerate": False,
        "data": {
            "login": "test3@example.com",
            "password": "password123",
            "project_id": uuid.uuid4(),
            "env_id": 1,
            "domain_id": 1,
        },
    }
    create_response = client.post("/users", json=user_data)
    user_id = create_response.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == HTTPStatus.OK
    assert "deleted_at" in response.json()


def test_acquire_release_lock(client):
    user_data = {
        "autogenerate": False,
        "data": {
            "login": "test4@example.com",
            "password": "secure1234",
            "project_id": uuid.uuid4(),
            "env_id": 1,
            "domain_id": 1,
        },
    }
    create_response = client.post("/users", json=user_data)
    user_id = create_response.json()["id"]

    acquire_response = client.patch(f"/users/{user_id}/acquire_lock")
    assert acquire_response.status_code == HTTPStatus.OK
    assert acquire_response.json()["locktime"] is not None

    release_response = client.patch(f"/users/{user_id}/release_lock")
    assert release_response.status_code == HTTPStatus.OK
    assert release_response.json()["locktime"] is None


if __name__ == "__main__":
    pytest.main()
