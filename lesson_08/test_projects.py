from uuid import uuid4

import pytest

from yougile_api import YouGileApi


@pytest.fixture
def api():
    return YouGileApi()


@pytest.fixture
def created_projects(api):
    project_ids = []

    yield project_ids

    for project_id in project_ids:
        api.delete_project(project_id)


def test_create_project_positive(api, created_projects):
    title = f"Autotest project {uuid4()}"

    response = api.create_project(title)

    assert response.status_code == 201
    project_id = response.json()["id"]
    created_projects.append(project_id)

    get_response = api.get_project(project_id)

    assert get_response.status_code == 200
    assert get_response.json()["id"] == project_id
    assert get_response.json()["title"] == title


def test_create_project_negative(api):
    response = api.create_project("")

    assert 400 <= response.status_code < 500
    assert response.json().get("error")


def test_update_project_positive(api, created_projects):
    initial_title = f"Initial project {uuid4()}"
    updated_title = f"Updated project {uuid4()}"

    create_response = api.create_project(initial_title)
    assert create_response.status_code == 201

    project_id = create_response.json()["id"]
    created_projects.append(project_id)

    response = api.update_project(project_id, updated_title)

    assert response.status_code == 200

    get_response = api.get_project(project_id)

    assert get_response.status_code == 200
    assert get_response.json()["id"] == project_id
    assert get_response.json()["title"] == updated_title


def test_update_project_negative(api):
    invalid_project_id = str(uuid4())

    response = api.update_project(
        invalid_project_id,
        "Updated project",
    )

    assert 400 <= response.status_code < 500
    assert response.json().get("error")


def test_get_project_positive(api, created_projects):
    title = f"Get project {uuid4()}"

    create_response = api.create_project(title)
    assert create_response.status_code == 201

    project_id = create_response.json()["id"]
    created_projects.append(project_id)

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id
    assert response.json()["title"] == title


def test_get_project_negative(api):
    invalid_project_id = str(uuid4())

    response = api.get_project(invalid_project_id)

    assert 400 <= response.status_code < 500
    assert response.json().get("error")
