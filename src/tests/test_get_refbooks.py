from datetime import datetime, timedelta
from urllib.parse import urlencode

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_refbooks_with_no_date(client):
    response = client.get(path=reverse("refbook-list"))
    assert response.status_code == 200
    assert response.json() == {
        "refbooks": [{"id": 1, "code": "1", "name": "refbook_1"}]
    }


@pytest.mark.django_db
def test_get_refbooks_with_date_1(client):
    date_param = {"date": (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")}
    query_string = urlencode(date_param)
    response = client.get(path=f'{reverse("refbook-list")}?{query_string}')
    assert response.status_code == 200
    assert response.json() == {
        "refbooks": [{"id": 1, "code": "1", "name": "refbook_1"}]
    }


@pytest.mark.django_db
def test_get_refbooks_with_date_2(client):
    date_param = {"date": (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")}
    query_string = urlencode(date_param)
    response = client.get(path=f'{reverse("refbook-list")}?{query_string}')
    assert response.status_code == 200
    assert response.json() == {"refbooks": []}


@pytest.mark.django_db
def test_get_refbooks_with_incorrect_date(client):
    date_param = {"date": "12345678"}
    query_string = urlencode(date_param)
    response = client.get(path=f'{reverse("refbook-list")}?{query_string}')
    assert response.status_code == 200
    assert response.json() == {
        "refbooks": [{"id": 1, "code": "1", "name": "refbook_1"}]
    }
