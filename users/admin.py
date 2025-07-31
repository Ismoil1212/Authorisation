from django.contrib import admin

from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_filter = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    search_fields = ["username", "first_name", "last_name", "email"]
    list_display_links = ["username", "email"]
    ordering = ["username"]
    fieldsets = (
        ("Основная информация", {"fields": ("username", "email")}),
        ("Личные данные", {"fields": ("first_name", "last_name")}),
    )
