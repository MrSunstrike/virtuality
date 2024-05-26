from django.db import models


class Effect(models.Model):
    class Stats(models.TextChoices):
        MAX_HP = ("max_hp", "Максимальный запас здоровья")
        CURRENT_HP = ("current_hp", "Текущий запас здоровья")
        MAX_MP = ("max_mp", "Максимальный запас маны")
        CURRENT_MP = ("current_mp", "Текущий запас маны")
        MAX_SP = ("max_sp", "Максимальный запас выносливости")
        CURRENT_SP = ("current_sp", "Текущий запас выносливости")
        PHYSICAL_DAMAGE = ("physical_damage", "Физический урон")
        MAGICAL_DAMAGE = ("magical_damage", "Магический урон")
        PHYSICAL_DEFENSE = ("physical_defense", "Защита от физического урона")
        MAGICAL_DEFENSE = ("magical_defense", "Защита от магического урона")
        REACTION_SPEED = ("reaction_speed", "Скорость реакции")
        MOVEMENT_SPEED = ("movement_speed", "Скорость передвижения")
        CRITICAL_HIT_CHANCE = ("critical_hit_chance", "Шанс на критический удар")
        PIERCING_CHANCE = ("pierce_chance", "Шанс на пронзающий удар")
        PHYSICAL_DAMAGE_BLOCK_CHANCE = ("physical_damage_block_chance", "Шанс на блокирование физического урона")
        PHYSICAL_DAMAGE_REFLECT_CHANCE = ("physical_damage_reflect_chance", "Шанс на отражение физического урона")
        DODGE_CHANCE = ("dodge_chance", "Шанс на уворот от атаки")
        LUCK = ("luck", "Удача")
        EXP = ("experience_points", "Опыт")
        LEVEL = ("level", "Уровень")

    class Direction(models.TextChoices):
        POSITIVE = ("positive", "Положительный")
        NEGATIVE = ("negative", "Отрицательный")

    class CalculationMethod(models.TextChoices):
        ADDITION = ("addition", "Сложение")
        MULTIPLICATION = ("multiplication", "Умножение")

    name = models.CharField(
        verbose_name="Название",
        max_length=100
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=300,
    )
    stat = models.CharField(
        verbose_name="Целевой показатель",
        choices=Stats.choices,
        max_length=30,
    )
    direction = models.CharField(
        verbose_name="Вектор",
        choices=Direction.choices,
        max_length=8,
    )
    calculation_method = models.CharField(
        verbose_name="Метод калькулирования",
        choices=CalculationMethod.choices,
        max_length=14,
    )
    value = models.FloatField(
        verbose_name="Значение",
    )
    duration = models.IntegerField(
        verbose_name="Длительность эффекта (ходов)"
    )

    class Meta:
        verbose_name = "Эффект"
        verbose_name_plural = "Эффекты"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
