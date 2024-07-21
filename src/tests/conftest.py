import pytest
from django.conf import settings
from rest_framework.test import APIClient

from src.main.models import ReferenceBook, ReferenceBookVersion, ReferenceBookElement
from src.tests import data_for_test_db


@pytest.fixture(scope="function")
def client():
    client = APIClient()
    yield client


@pytest.fixture(scope="function", autouse=True)
def create_test_records():
    data_for_test_db.refbook.save()
    ReferenceBookVersion.objects.bulk_create(data_for_test_db.refbook_versions)
    ReferenceBookElement.objects.bulk_create(data_for_test_db.refbook_elements)


@pytest.fixture()
def create_refbook():
    def create_refbook(id, code, title, description):
        return ReferenceBook.objects.create(
            id=id, code=code, title=title, description=description
        )

    return create_refbook


@pytest.fixture
def create_refbook_version():
    def create_refbook_version(id, reference_book_id, version, start_date):
        return ReferenceBookVersion.objects.create(
            id=id,
            reference_book_id=reference_book_id,
            version=version,
            start_date=start_date,
        )

    return create_refbook_version


@pytest.fixture
def create_refbook_element():
    def create_refbook_element(id, reference_book_version_id, code, value):
        return ReferenceBookVersion.objects.create(
            id=id,
            reference_book_version_id=reference_book_version_id,
            code=code,
            value=value,
        )

    return create_refbook_element
