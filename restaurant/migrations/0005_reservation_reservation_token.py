# Generated by Django 4.2.2 on 2024-09-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0004_alter_reservation_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="reservation_token",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Reservation token"
            ),
        ),
    ]
