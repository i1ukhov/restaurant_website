# Generated by Django 4.2.2 on 2024-09-02 22:09

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_alter_reservation_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="time",
            field=multiselectfield.db.fields.MultiSelectField(
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
                help_text="Выберите слоты по времени (до 4-х слотов)",
                max_length=40,
                verbose_name="Время",
            ),
        ),
    ]
