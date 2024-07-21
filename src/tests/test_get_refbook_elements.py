import pytest
from django.urls import reverse
from urllib.parse import urlencode


@pytest.mark.django_db
def test_get_elements_with_no_version(client):
    base_url = reverse("refbook-elements", kwargs={"id": 1})
    response = client.get(path=base_url)
    assert response.status_code == 200
    assert response.json() == {
        "elements": [{"code": "1-1", "value": "1-1"}, {"code": "1-2", "value": "1-2"}]
    }


@pytest.mark.django_db
def test_get_elements_with_version(client):
    version_param = {"version": "2.0"}
    query_string = urlencode(version_param)
    base_url = reverse("refbook-elements", kwargs={"id": 1})
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 200
    assert response.json() == {
        "elements": [{"code": "2-1", "value": "2-1"}, {"code": "2-2", "value": "2-2"}]
    }


@pytest.mark.django_db
def test_get_elements_from_non_existing_refbook(client):
    base_url = reverse("refbook-elements", kwargs={"id": 3})
    response = client.get(path=base_url)
    assert response.status_code == 404
    assert response.json() == {"detail": "No ReferenceBook matches the given query."}


@pytest.mark.django_db
def test_get_elements_with_non_existing_version(client):
    version_param = {"version": "3.0"}
    query_string = urlencode(version_param)
    base_url = reverse("refbook-elements", kwargs={"id": 1})
    response = client.get(path=f"{base_url}?{query_string}")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "No ReferenceBookVersion matches the given query."
    }
