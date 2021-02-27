from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email']


# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model
admin.site.register(User, UserAdmin)
