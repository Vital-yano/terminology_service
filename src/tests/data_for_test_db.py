from datetime import datetime, timedelta

from src.main.models import ReferenceBook, ReferenceBookVersion, ReferenceBookElement

REFBOOK_DATA = {
    "id": 1,
    "code": "1",
    "name": "refbook_1",
    "description": "refbook_1",
}
REFBOOK_VERSION_DATA_1 = {
    "id": 1,
    "reference_book_id": 1,
    "version": "1.0",
    "start_date": datetime.today(),
}
REFBOOK_VERSION_DATA_2 = {
    "id": 2,
    "reference_book_id": 1,
    "version": "2.0",
    "start_date": datetime.today() + timedelta(days=7),
}
REFBOOK_ELEMENTS_DATA_1 = {
    "id": 1,
    "reference_book_version_id": 1,
    "code": "1-1",
    "value": "1-1",
}
REFBOOK_ELEMENTS_DATA_2 = {
    "id": 2,
    "reference_book_version_id": 1,
    "code": "1-2",
    "value": "1-2",
}
REFBOOK_ELEMENTS_DATA_3 = {
    "id": 3,
    "reference_book_version_id": 2,
    "code": "2-1",
    "value": "2-1",
}
REFBOOK_ELEMENTS_DATA_4 = {
    "id": 4,
    "reference_book_version_id": 2,
    "code": "2-2",
    "value": "2-2",
}

refbook = ReferenceBook(**REFBOOK_DATA)
refbook_versions = [
    ReferenceBookVersion(**REFBOOK_VERSION_DATA_1),
    ReferenceBookVersion(**REFBOOK_VERSION_DATA_2),
]
refbook_elements = [
    ReferenceBookElement(**REFBOOK_ELEMENTS_DATA_1),
    ReferenceBookElement(**REFBOOK_ELEMENTS_DATA_2),
    ReferenceBookElement(**REFBOOK_ELEMENTS_DATA_3),
    ReferenceBookElement(**REFBOOK_ELEMENTS_DATA_4),
]
