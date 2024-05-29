from django.contrib import admin

from apps.avatar.models import Avatar, AvatarStats, Skill, Specialization, Species, SpeciesLevelUpStats


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    pass


@admin.register(AvatarStats)
class AvatarStatsAdmin(admin.ModelAdmin):
    pass


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(SpeciesLevelUpStats)
class SpeciesLevelUpStatsAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
