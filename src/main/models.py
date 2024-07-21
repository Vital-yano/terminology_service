from django.core.exceptions import ValidationError
from django.db import models


class ReferenceBook(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=300)
    description = models.TextField()

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"

    def __str__(self):
        return f"Справочник {self.name}"


class ReferenceBookVersion(models.Model):
    reference_book = models.ForeignKey(
        ReferenceBook, related_name="versions", on_delete=models.CASCADE
    )
    version = models.CharField(max_length=50)
    start_date = models.DateField()

    class Meta:
        verbose_name = "Версия справочника"
        verbose_name_plural = "Версии справочника"

        constraints = [
            models.UniqueConstraint(
                fields=["reference_book_id", "version"],
                name="unique_reference_book_id_and_version",
            )
        ]

    def __str__(self):
        return f"Версия {self.version} - {self.reference_book}"

    def clean(self):
        if (
            ReferenceBookVersion.objects.filter(
                reference_book=self.reference_book, start_date=self.start_date
            )
            .exclude(id=self.id)
            .exists()
        ):
            raise ValidationError(
                'У одного Справочника не может быть более одной версии с одинаковой "Датой начала".'
            )


class ReferenceBookElement(models.Model):
    reference_book_version = models.ForeignKey(
        ReferenceBookVersion, related_name="elements", on_delete=models.CASCADE
    )
    code = models.CharField(max_length=100)
    value = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"

        constraints = [
            models.UniqueConstraint(
                fields=["reference_book_version_id", "code"],
                name="unique_reference_book_version_id_and_code",
            )
        ]

    def __str__(self):
        return f"Элемент {self.code} - {self.value}"
