from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_id = models.BigIntegerField(
        verbose_name="Telegram ID",
        unique=True,
        blank=True,
        null=True
    )
