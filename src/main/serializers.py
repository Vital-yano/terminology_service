from rest_framework import serializers

from .models import ReferenceBook, ReferenceBookElement


class RefBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceBook
        fields = ["id", "code", "name"]


class RefBookElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceBookElement
        fields = ["code", "value"]
