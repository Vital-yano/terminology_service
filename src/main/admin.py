from django.contrib import admin

from .models import ReferenceBook, ReferenceBookElement, ReferenceBookVersion


class RefBookElementInline(admin.TabularInline):
    model = ReferenceBookElement
    extra = 1
    fields = ["code", "value"]

    def has_add_permission(self, request, obj=None):
        if obj:
            return super().has_add_permission(request, obj)
        return False


class RefBookVersionInline(admin.TabularInline):
    model = ReferenceBookVersion
    extra = 1
    fields = ["version", "start_date"]
    show_change_link = True

    def has_add_permission(self, request, obj=None):
        if obj:
            return super().has_add_permission(request, obj)
        return False


@admin.register(ReferenceBookVersion)
class RefBookVersionAdmin(admin.ModelAdmin):
    list_display = ["refbook_code", "refbook_name", "version", "start_date"]
    fields = ["reference_book", "version", "start_date"]
    inlines = [RefBookElementInline]

    def refbook_code(self, obj):
        return obj.reference_book.code

    refbook_code.short_description = "Код справочника"

    def refbook_name(self, obj):
        return obj.reference_book.name

    refbook_name.short_description = "Наименование справочника"


@admin.register(ReferenceBook)
class RefBookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "code",
        "name",
        "current_version",
        "current_version_start_date",
    ]
    fields = ["code", "name", "description"]
    inlines = [RefBookVersionInline]

    def current_version(self, obj):
        current_version = obj.versions.order_by("-start_date").first()
        return current_version.version if current_version else "Нет версий"

    current_version.short_description = "Текущая версия"

    def current_version_start_date(self, obj):
        current_version = obj.versions.order_by("-start_date").first()
        return current_version.start_date if current_version else "Нет версий"

    current_version_start_date.short_description = "Дата начала текущей версии"
