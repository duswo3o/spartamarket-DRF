# Generated by Django 4.2 on 2024-09-08 07:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0002_product_like_users"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hashtag",
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
                    "tag",
                    models.CharField(max_length=20, unique=True, verbose_name="tag"),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="like_users",
            field=models.ManyToManyField(
                blank=True, related_name="like_products", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="product_tags",
                to="products.hashtag",
                verbose_name="해시태그 목록",
            ),
        ),
    ]
