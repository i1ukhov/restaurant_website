# Generated by Django 4.2.2 on 2024-09-01 18:19

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        help_text="Укажите дату бронирования",
                        verbose_name="Дата бронирования",
                    ),
                ),
                (
                    "table",
                    models.CharField(
                        choices=[
                            ("1A", "№1 веранда"),
                            ("2A", "№2 веранда"),
                            ("3A", "№3 веранда"),
                            ("4A", "№4 веранда"),
                            ("5A", "№5 веранда"),
                            ("6A", "№6 веранда"),
                            ("1B", "№1 зал"),
                            ("2B", "№2 зал"),
                            ("3B", "№3 зал"),
                            ("4B", "№4 зал"),
                            ("5B", "№5 зал"),
                            ("6B", "№6 зал"),
                            ("7B", "№7 зал"),
                            ("8B", "№8 зал"),
                            ("9B", "№9 зал"),
                            ("10B", "№10 зал"),
                        ],
                        help_text="Выберите столик",
                        max_length=5,
                        verbose_name="Столик",
                    ),
                ),
                (
                    "time",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("9", "9:00 - 10:00"),
                            ("10", "10:00 - 11:00"),
                            ("11", "11:00 - 12:00"),
                            ("12", "12:00 - 13:00"),
                            ("13", "13:00 - 14:00"),
                            ("14", "14:00 - 15:00"),
                            ("15", "15:00 - 16:00"),
                            ("16", "16:00 - 17:00"),
                            ("17", "17:00 - 18:00"),
                            ("18", "18:00 - 19:00"),
                            ("19", "19:00 - 20:00"),
                            ("20", "20:00 - 21:00"),
                            ("21", "21:00 - 22:00"),
                            ("22", "22:00 - 23:00"),
                        ],
                        max_length=40,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Создана"),
                            ("confirmed", "Подтверждена"),
                            ("completed", "Завершена"),
                            ("canceled", "Отменена"),
                        ],
                        default="created",
                        help_text="Укажите статус бронирования",
                        max_length=20,
                        verbose_name="Статус бронирования",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Укажите клиента",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Клиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Бронь",
                "verbose_name_plural": "Брони",
            },
        ),
    ]
