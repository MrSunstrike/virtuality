from apps.user.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class AvatarStatsAdmin(UserAdmin):
    pass
