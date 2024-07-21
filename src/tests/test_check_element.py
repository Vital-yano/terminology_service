from urllib.parse import urlencode

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_check_element_with_no_version(client):
    base_url = reverse("check-element", kwargs={"id": 1})
    query_params = {"code": "1-1", "value": "1-1"}
    query_string = urlencode(query_params)
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 200
    assert response.json() == {"element_exists": True}


@pytest.mark.django_db
def test_check_element_with_version_1(client):
    base_url = reverse("check-element", kwargs={"id": 1})
    query_params = {"code": "1-1", "value": "1-1", "version": "1.0"}
    query_string = urlencode(query_params)
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 200
    assert response.json() == {"element_exists": True}


@pytest.mark.django_db
def test_check_element_with_version_2(client):
    base_url = reverse("check-element", kwargs={"id": 1})
    query_params = {"code": "1-1", "value": "1-1", "version": "2.0"}
    query_string = urlencode(query_params)
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 200
    assert response.json() == {"element_exists": False}


@pytest.mark.django_db
def test_check_element_with_non_existing_refbook_id(client):
    base_url = reverse("check-element", kwargs={"id": 3})
    query_params = {"code": "1-1", "value": "1-1", "version": "2.0"}
    query_string = urlencode(query_params)
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 404
    assert response.json() == {"detail": "No ReferenceBook matches the given query."}


@pytest.mark.django_db
def test_check_element_without_code(client):
    base_url = reverse("check-element", kwargs={"id": 3})
    query_params = {"value": "1-1", "version": "2.0"}
    query_string = urlencode(query_params)
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Missing required query parameters: code and value"
    }


@pytest.mark.django_db
def test_check_element_without_value(client):
    base_url = reverse("check-element", kwargs={"id": 3})
    query_params = {"code": "1-1", "version": "2.0"}
    query_string = urlencode(query_params)
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Missing required query parameters: code and value"
    }
