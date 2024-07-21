from drf_yasg import openapi

detail_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "detail": openapi.Schema(
            type=openapi.TYPE_STRING, description="A detailed message"
        )
    },
)

element_existence_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "element_exists": openapi.Schema(
            type=openapi.TYPE_STRING, description="Message about element existence"
        )
    },
)
code_param = openapi.Parameter(
    "code",
    openapi.IN_QUERY,
    description="element code",
    type=openapi.TYPE_STRING,
    required=True,
)

value_param = openapi.Parameter(
    "value",
    openapi.IN_QUERY,
    description="element value",
    type=openapi.TYPE_STRING,
    required=True,
)

date_param = openapi.Parameter(
    "date",
    openapi.IN_QUERY,
    description="date",
    type=openapi.TYPE_STRING,
    required=False,
)

version_param = openapi.Parameter(
    "version",
    openapi.IN_QUERY,
    description="refbook version",
    type=openapi.TYPE_STRING,
    required=False,
)

response_200 = openapi.Response(
    "OK",
    examples={
        "application/json": {
            "element_exists": {"element_exists": "true"},
            "elements_doesnt_exist": {"element_exists": "false"},
        }
    },
    schema=element_existence_schema,
)

response_400 = openapi.Response(
    "Bad Request",
    examples={
        "application/json": {
            "refbook_notfound_example": {
                "detail": "Missing required query parameters: code and value"
            }
        }
    },
    schema=detail_schema,
)

response_404 = openapi.Response(
    "Not Found",
    examples={
        "application/json": {
            "refbook_notfound_example": {
                "detail": "No ReferenceBook matches the given query."
            },
            "refbook_version_not_found_example": {
                "detail": "No ReferenceBookVersion matches the given query."
            },
        }
    },
    schema=detail_schema,
)
