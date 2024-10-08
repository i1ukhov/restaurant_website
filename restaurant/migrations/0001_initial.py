# Generated by Django 5.1 on 2024-08-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dish",
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
                    "name",
                    models.CharField(
                        help_text="Введите название блюда",
                        max_length=100,
                        verbose_name="Название блюда",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фотографию блюда",
                        null=True,
                        upload_to="restaurant/images",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание блюда",
                        null=True,
                        verbose_name="Описание блюда",
                    ),
                ),
                (
                    "ingredients",
                    models.TextField(
                        blank=True,
                        help_text="Введите состав блюда",
                        null=True,
                        verbose_name="Состав",
                    ),
                ),
                (
                    "weight",
                    models.PositiveIntegerField(
                        help_text="Укажите вес блюда в граммах",
                        verbose_name="Вес блюда",
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        help_text="Укажите цену блюда в рублях", verbose_name="Цена"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("appetisers", "Закуски"),
                            ("breakfasts", "Завтраки"),
                            ("salads", "Салаты"),
                            ("cold side dish", "Холодные блюда"),
                            ("hot side dish", "Горячие блюда"),
                            ("desserts", "Десерты"),
                            ("drinks", "Напитки"),
                            ("extra", "Дополнительно"),
                        ],
                        help_text="Выберите категорию",
                        max_length=25,
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блюдо",
                "verbose_name_plural": "Блюда",
            },
        ),
    ]
