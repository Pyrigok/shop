from django.contrib import admin

from users_app.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "role", "date_joined", "is_active"]
    ordering = ("is_active",)
    exclude = ("password",)

admin.site.register(User, UserAdmin)
