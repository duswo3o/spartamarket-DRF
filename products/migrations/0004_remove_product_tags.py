# Generated by Django 4.2 on 2024-09-08 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_hashtag_alter_product_like_users_product_tags"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="tags",
        ),
    ]
