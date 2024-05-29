from apps.common.models import Effect
from apps.user.models import User
from django.db import models


class SpeciesLevelUpStats(models.Model):
    """
    Модель, представляющая схему увеличения характеристик для вида при повышении уровня.
    """
    max_hp_increase = models.PositiveIntegerField(
        verbose_name="Максимальный запас здоровья",
    )
    max_mp_increase = models.PositiveIntegerField(
        verbose_name="Максимальный запас маны",
    )
    max_sp_increase = models.PositiveIntegerField(
        verbose_name="Максимальный запас выносливости",
    )
    physical_damage_increase = models.PositiveIntegerField(
        verbose_name="Физический урон",
    )
    magical_damage_increase = models.FloatField(
        verbose_name="Магический урон",
    )
    physical_defense_increase = models.PositiveIntegerField(
        verbose_name="Защита от физического урона",
    )
    magical_defense_increase = models.FloatField(
        verbose_name="Защита от магического урона",
    )
    reaction_speed_increase = models.PositiveIntegerField(
        verbose_name="Скорость реакции",
    )
    movement_speed_increase = models.PositiveIntegerField(
        verbose_name="Скорость передвижения",
    )
    critical_hit_chance_increase = models.FloatField(
        verbose_name="Шанс на критический удар",
    )
    pierce_chance_increase = models.FloatField(
        verbose_name="Шанс на пронзающий удар",
    )
    physical_damage_block_chance_increase = models.FloatField(
        verbose_name="Шанс на блокирование физического урона",
    )
    physical_damage_reflect_chance_increase = models.FloatField(
        verbose_name="Шанс на отражение физического урона",
    )
    dodge_chance_increase = models.FloatField(
        verbose_name="Шанс на уворот от атаки",
    )
    luck_increase = models.FloatField(
        verbose_name="Удача",
    )

    class Meta:
        verbose_name = "Схема увеличения характеристик"
        verbose_name_plural = "Схемы увеличения характеристик"


class Species(models.Model):
    """
    Модель, представляющая вид питомца.
    """
    name = models.CharField(
        verbose_name="Название",
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        max_length=1000,
    )
    enhancement_stats = models.OneToOneField(
        verbose_name="Улучшение характеристик",
        to=SpeciesLevelUpStats,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="images/species/",
    )

    class Meta:
        verbose_name = "Вид питомца"
        verbose_name_plural = "Виды питомцев"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Specialization(models.Model):
    """
    Модель, представляющая специализацию.
    """
    title = models.CharField(
        verbose_name="Название",
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        max_length=1000,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="images/specializations/",
    )

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    """
    Модель, представляющая навык.
    """
    avatar_specialization = models.ForeignKey(
        verbose_name="Специализация",
        to=Specialization,
        on_delete=models.CASCADE,
        related_name="skills",
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=100,
        unique=True,
    )
    effect = models.ForeignKey(
        verbose_name="Эффект",
        to=Effect,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name="Пиктограмма",
        upload_to="images/skills/",
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ["title"]

    def __str__(self):
        return self.title


class AvatarStats(models.Model):
    """
    Модель, представляющая характеристики питомца.
    """
    max_hp = models.IntegerField(verbose_name="Максимальный запас здоровья")
    current_hp = models.IntegerField(verbose_name="Текущий запас здоровья")

    max_mp = models.IntegerField(verbose_name="Максимальный запас маны")
    current_mp = models.IntegerField(verbose_name="Текущий запас маны")

    max_sp = models.IntegerField(verbose_name="Максимальный запас выносливости")
    current_sp = models.IntegerField(verbose_name="Текущий запас выносливости")

    satiety = models.IntegerField(verbose_name="Сытость")

    physical_damage = models.IntegerField(verbose_name="Физический урон")
    magical_damage = models.FloatField(verbose_name="Магический урон")

    physical_defense = models.IntegerField(verbose_name="Защита от физического урона")
    magical_defense = models.FloatField(verbose_name="Защита от магического урона")

    reaction_speed = models.IntegerField(verbose_name="Скорость реакции")
    movement_speed = models.IntegerField(verbose_name="Скорость передвижения")

    critical_hit_chance = models.FloatField(verbose_name="Шанс на критический удар")
    pierce_chance = models.FloatField(verbose_name="Шанс на пронзающий удар")

    physical_damage_block_chance = models.FloatField(verbose_name="Шанс на блокирование физического урона")
    physical_damage_reflect_chance = models.FloatField(verbose_name="Шанс на отражение физического урона")
    dodge_chance = models.FloatField(verbose_name="Шанс на уворот от атаки")

    luck = models.FloatField(verbose_name="Удача")

    experience_points = models.IntegerField(verbose_name="Опыт")
    level = models.IntegerField(verbose_name="Уровень")

    class Meta:
        verbose_name = "Характеристики питомца"
        verbose_name_plural = "Характеристики питомцев"


class Avatar(models.Model):
    """
    Модель, представляющая питомца.
    """
    class AvatarGender(models.TextChoices):
        MALE = "M", "Самец"
        FEMALE = "F", "Самка"

    name = models.CharField(
        verbose_name="Имя",
        max_length=100,
        unique=True,
    )
    gender = models.CharField(
        verbose_name="Пол",
        max_length=1,
        choices=AvatarGender.choices,
    )
    species = models.ForeignKey(
        to=Species,
        verbose_name="Вид",
        on_delete=models.PROTECT,
        related_name="avatars",
    )
    specialization = models.ForeignKey(
        to=Specialization,
        verbose_name="Специализация",
        on_delete=models.PROTECT,
        related_name="avatars",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        to=User,
        verbose_name="Хозяин",
        on_delete=models.CASCADE,
        related_name="avatars",
    )

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return f"{self.species} {self.name} - {self.specialization}"
