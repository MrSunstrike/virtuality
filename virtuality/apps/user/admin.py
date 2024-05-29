from django.contrib.auth.admin import UserAdmin

from apps.user.models import User
from django.contrib import admin


@admin.register(User)
class AvatarStatsAdmin(UserAdmin):
    pass
