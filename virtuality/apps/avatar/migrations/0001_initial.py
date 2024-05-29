# Generated by Django 5.0.6 on 2024-05-29 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_alter_effect_stat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_hp', models.IntegerField(verbose_name='Максимальный запас здоровья')),
                ('current_hp', models.IntegerField(verbose_name='Текущий запас здоровья')),
                ('max_mp', models.IntegerField(verbose_name='Максимальный запас маны')),
                ('current_mp', models.IntegerField(verbose_name='Текущий запас маны')),
                ('max_sp', models.IntegerField(verbose_name='Максимальный запас выносливости')),
                ('current_sp', models.IntegerField(verbose_name='Текущий запас выносливости')),
                ('satiety', models.IntegerField(verbose_name='Сытость')),
                ('physical_damage', models.IntegerField(verbose_name='Физический урон')),
                ('magical_damage', models.FloatField(verbose_name='Магический урон')),
                ('physical_defense', models.IntegerField(verbose_name='Защита от физического урона')),
                ('magical_defense', models.FloatField(verbose_name='Защита от магического урона')),
                ('reaction_speed', models.IntegerField(verbose_name='Скорость реакции')),
                ('movement_speed', models.IntegerField(verbose_name='Скорость передвижения')),
                ('critical_hit_chance', models.FloatField(verbose_name='Шанс на критический удар')),
                ('pierce_chance', models.FloatField(verbose_name='Шанс на пронзающий удар')),
                ('physical_damage_block_chance', models.FloatField(verbose_name='Шанс на блокирование физического урона')),
                ('physical_damage_reflect_chance', models.FloatField(verbose_name='Шанс на отражение физического урона')),
                ('dodge_chance', models.FloatField(verbose_name='Шанс на уворот от атаки')),
                ('luck', models.FloatField(verbose_name='Удача')),
                ('experience_points', models.IntegerField(verbose_name='Опыт')),
                ('level', models.IntegerField(verbose_name='Уровень')),
            ],
            options={
                'verbose_name': 'Характеристики питомца',
                'verbose_name_plural': 'Характеристики питомцев',
            },
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/specializations/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/species/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Вид питомца',
                'verbose_name_plural': 'Виды питомцев',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SpeciesLevelUpStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_hp_increase', models.PositiveIntegerField(verbose_name='Максимальный запас здоровья')),
                ('max_mp_increase', models.PositiveIntegerField(verbose_name='Максимальный запас маны')),
                ('max_sp_increase', models.PositiveIntegerField(verbose_name='Максимальный запас выносливости')),
                ('physical_damage_increase', models.PositiveIntegerField(verbose_name='Физический урон')),
                ('magical_damage_increase', models.FloatField(verbose_name='Магический урон')),
                ('physical_defense_increase', models.PositiveIntegerField(verbose_name='Защита от физического урона')),
                ('magical_defense_increase', models.FloatField(verbose_name='Защита от магического урона')),
                ('reaction_speed_increase', models.PositiveIntegerField(verbose_name='Скорость реакции')),
                ('movement_speed_increase', models.PositiveIntegerField(verbose_name='Скорость передвижения')),
                ('critical_hit_chance_increase', models.FloatField(verbose_name='Шанс на критический удар')),
                ('pierce_chance_increase', models.FloatField(verbose_name='Шанс на пронзающий удар')),
                ('physical_damage_block_chance_increase', models.FloatField(verbose_name='Шанс на блокирование физического урона')),
                ('physical_damage_reflect_chance_increase', models.FloatField(verbose_name='Шанс на отражение физического урона')),
                ('dodge_chance_increase', models.FloatField(verbose_name='Шанс на уворот от атаки')),
                ('luck_increase', models.FloatField(verbose_name='Удача')),
            ],
            options={
                'verbose_name': 'Схема увеличения характеристик',
                'verbose_name_plural': 'Схемы увеличения характеристик',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/skills/', verbose_name='Пиктограмма')),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.effect', verbose_name='Эффект')),
                ('avatar_specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='avatar.specialization', verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('gender', models.CharField(choices=[('M', 'Самец'), ('F', 'Самка')], max_length=1, verbose_name='Пол')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatars', to=settings.AUTH_USER_MODEL, verbose_name='Хозяин')),
                ('specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avatars', to='avatar.specialization', verbose_name='Специализация')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='avatars', to='avatar.species', verbose_name='Вид')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
        migrations.AddField(
            model_name='species',
            name='enhancement_stats',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='avatar.specieslevelupstats', verbose_name='Улучшение характеристик'),
        ),
    ]
