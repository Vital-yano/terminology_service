from django.urls import path

from .views import CheckRefBookElementView, RefBookElementsView, RefBookListView

urlpatterns = [
    path("", RefBookListView.as_view(), name="refbook-list"),
    path("<int:id>/elements/", RefBookElementsView.as_view(), name="refbook-elements"),
    path(
        "<int:id>/check_element/",
        CheckRefBookElementView.as_view(),
        name="check-element",
    ),
]
