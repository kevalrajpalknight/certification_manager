from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserModelAdmin(UserAdmin):
    empty_value_display = "-empty-"
    fieldsets = [
        (
            _("Details"),
            {
                "fields": [
                    "name",
                    "email",
                    "phone",
                    "password",
                ]
            },
        ),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_superuser",
                ]
            },
        ),
        (
            _("Additional Information"),
            {
                "fields": [
                    "last_login",
                    "date_joined",
                ]
            },
        ),
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": [
                    "name",
                    "email",
                    "password1",
                    "password2",
                ],
            },
        ),
    )
    exclude = ["username"]
    readonly_fields = ["is_superuser", "last_login", "date_joined"]
    list_display = [
        "name",
        "email",
    ]
    list_display_links = ["email"]
    ordering = ["name", "email"]
    list_filter = [
        "is_superuser",
    ]
    filter_horizontal = []
    search_fields = ["email", "name", "id"]
    actions = None

    def has_delete_permission(self, request, obj=None):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return super().has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return super().has_change_permission(request, obj)


admin.site.register(User, UserModelAdmin)
