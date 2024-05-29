from apps.common.models import Effect
from django.contrib import admin


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
    pass
