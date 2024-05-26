from apps.user.models import User
from django.db import models


class SpeciesEnhancement(models.Model):
    pass


class Species(models.Model):
    name = models.CharField(
        verbose_name="Название вида",
        max_length=100,
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описание вида",
        max_length=1000,
    )
    enhancement_stats = models.OneToOneField(
        verbose_name="Улучшение характеристик",
        to=SpeciesEnhancement,
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
    pass


class Skill(models.Model):
    pass


class AvatarStats(models.Model):
    pass


class Avatar(models.Model):
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
