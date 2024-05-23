from django.db import models


class Stats(models.TextChoices):
    MAX_HP = ("max_hp", "Максимальный запас здоровья")
    MAX_MP = ("max_mp", "Максимальный запас маны")
    MAX_SP = ("max_sp", "Максимальный запас выносливости")
    PHYSICAL_DAMAGE = ("phys_dmg", "Физический урон")
    MAGICAL_DAMAGE = ("mgc_dmg", "Магический урон")
    PHYSICAL_DEFENSE = ("phys_def", "Защита от физического урона")
    MAGICAL_DEFENSE = ("mgc_def", "Защита от магического урона")
    REACTION_SPEED = ("reaction", "Скорость реакции")
    MOVEMENT_SPEED = ("mv_speed", "Скорость передвижения")
    CRITICAL_HIT_CHANCE = ("crit_chance", "Шанс на критический удар")
    PIERCING_CHANCE = ("pierce_chane", "Шанс на пронзающий удар")
    PHYSICAL_DAMAGE_BLOCK_CHANCE = ("phys_dmg_block_chance", "Шанс на блокирование физического урона")
    PHYSICAL_DAMAGE_REFLECT_CHANCE = ("phys_dmg_reflect_chance", "Шанс на отражение физического урона")
    DODGE_CHANCE = ("dodge_chance", "Шанс на уворот от атаки")
    LUCK = ("luck", "Удача")
