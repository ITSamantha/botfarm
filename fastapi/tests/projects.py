import random
import pytest
from fastapi.testclient import TestClient
from http import HTTPStatus
from src.main import get_application


@pytest.fixture
def client():
    app = get_application()
    with TestClient(app) as client:
        yield client


def test_get_projects(client):
    response = client.get("/projects")
    assert response.status_code == HTTPStatus.OK
    assert isinstance(response.json(), list)


def test_create_project(client):
    number = random.randint(1, 1000)
    project = {"title": f"test project {number}"}
    response = client.post("/projects", json=project)
    assert response.status_code == HTTPStatus.OK
    assert project["title"] == response.json()["title"]
    client.delete(f"/projects/{response.json()["id"]}")


def test_get_project_by_id(client):
    number = random.randint(1, 1000)
    project = {"title": f"test project {number}"}
    create_response = client.post("/projects", json=project)
    project_id = create_response.json()["id"]

    response = client.get(f"/projects/{project_id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json()["id"] == project_id

    client.delete(f"/projects/{response.json()["id"]}")


def test_delete_project(client):
    number = random.randint(1, 1000)
    project = {"title": f"test project {number}"}
    create_response = client.post("/projects", json=project)
    project_id = create_response.json()["id"]

    response = client.delete(f"/projects/{project_id}")
    assert response.status_code == HTTPStatus.OK


if __name__ == "__main__":
    pytest.main()
