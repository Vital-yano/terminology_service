from datetime import datetime

from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import ReferenceBook, ReferenceBookElement, ReferenceBookVersion


def get_current_version(version_param, refbook):
    if version_param:
        version = get_object_or_404(
            ReferenceBookVersion, reference_book=refbook, version=version_param
        )
    else:
        today = datetime.today()
        version = (
            ReferenceBookVersion.objects.filter(
                reference_book=refbook, start_date__lte=today
            )
            .order_by("-start_date")
            .first()
        )
    return version


def get_refbooks(request):
    queryset = ReferenceBook.objects.all().prefetch_related("versions")

    date_str = request.query_params.get("date", None)
    if date_str:
        date = parse_date(date_str)
        if date:
            queryset = queryset.filter(versions__start_date__lte=date)
    return queryset


def get_refbook_elements(kwargs, request):
    refbook_id = kwargs.get("id")
    version_param = request.query_params.get("version", None)

    refbook = get_object_or_404(ReferenceBook, id=refbook_id)
    version = get_current_version(version_param, refbook)

    if not version:
        raise NotFound("No valid version found for the given RefBook")

    return ReferenceBookElement.objects.filter(
        reference_book_version=version
    ).select_related("reference_book_version")


def check_element(kwargs, request):
    refbook_id = kwargs.get("id")
    code = request.query_params.get("code")
    value = request.query_params.get("value")
    version_param = request.query_params.get("version", None)

    if not code or not value:
        return Response(
            {"detail": "Missing required query parameters: code and value"},
            status=400,
        )

    refbook = get_object_or_404(ReferenceBook, id=refbook_id)
    version = get_current_version(version_param, refbook)

    if not version:
        raise NotFound("No valid version found for the given RefBook")

    element_exists = ReferenceBookElement.objects.filter(
        reference_book_version=version, code=code, value=value
    ).exists()
    return Response({"element_exists": element_exists})
