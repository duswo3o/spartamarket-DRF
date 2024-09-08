from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        to=get_user_model(), related_name="product", on_delete=models.CASCADE
    )

    like_users = models.ManyToManyField(
        to=get_user_model(),
        related_name="like_products",
        blank=True,
    )

    tags = models.ManyToManyField(
        to="products.Hashtag",
        verbose_name="해시태그 목록",
        blank=True,
        related_name="product_tags",
    )

    def __str__(self):
        return self.title


class Hashtag(models.Model):
    tag = models.CharField("tag", max_length=20, unique=True)

    def __str__(self):
        return self.tag
