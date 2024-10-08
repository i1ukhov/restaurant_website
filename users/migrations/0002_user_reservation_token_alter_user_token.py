# Generated by Django 4.2.2 on 2024-09-02 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reservation_token",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Reservation token"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Token"
            ),
        ),
    ]
