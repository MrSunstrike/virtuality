from django.db import models

from apps.user.models import User


class Species(models.Model):
    pass


class Specialization(models.Model):
    pass


class Skill(models.Model):
    pass


class AvatarStats(models.Model):
    pass


class BoostStatsPerLevel(models.Model):
    pass


class Avatar(models.Model):
    class AvatarGender(models.TextChoices):
        MALE = "M", "Самец"
        FEMALE = "F", "Самка"

    name = models.CharField(
        verbose_name="Имя",
        max_length=100,
    )
    gender = models.CharField(
        verbose_name="Пол",
        max_length=1,
        choices=AvatarGender
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
