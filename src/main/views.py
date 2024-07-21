from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response

from .openapi_spec import (
    code_param,
    date_param,
    response_200,
    response_400,
    response_404,
    value_param,
    version_param,
)
from .serializers import RefBookElementsSerializer, RefBookSerializer
from .services import check_element, get_refbook_elements, get_refbooks


class RefBookListView(generics.ListAPIView):
    serializer_class = RefBookSerializer

    def get_queryset(self):
        return get_refbooks(self.request)

    @swagger_auto_schema(manual_parameters=[date_param])
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"refbooks": serializer.data})


class RefBookElementsView(generics.ListAPIView):
    serializer_class = RefBookElementsSerializer

    def get_queryset(self):
        return get_refbook_elements(self.kwargs, self.request)

    @swagger_auto_schema(
        manual_parameters=[version_param], responses={404: response_404}
    )
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"elements": serializer.data})


class CheckRefBookElementView(generics.GenericAPIView):
    @swagger_auto_schema(
        manual_parameters=[code_param, value_param, version_param],
        responses={200: response_200, 400: response_400, 404: response_404},
    )
    def get(self, request, *args, **kwargs):
        return check_element(self.kwargs, request)
