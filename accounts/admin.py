from django.contrib import admin

from accounts.models import Organization
from accounts.models import User


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "abbr",
        "name",
        "industry",
        "registered_country",
        "last_modified",
        "created",
    )
    list_display_links = ("abbr",)
    search_fields = ("abbr", "name", "id")
    list_filter = (
        "industry",
        "registered_country",
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "organization",
        "first_name",
        "last_name",
        "last_modified",
        "created",
    )

    list_filter = ("organization",)

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )
