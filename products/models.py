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

    def __str__(self):
        return self.title
