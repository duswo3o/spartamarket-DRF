from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(get_user_model(), related_name="product", on_delete=models.CASCADE)

    like_users = models.ManyToManyField(get_user_model(), related_name='like_products')
    tags = models.ManyToManyField("products.Hashtag", verbose_name="해시태그 목록", blank=True, related_name='product_tags')


class Hashtag(models.Model):
    tag = models.CharField("tag", max_length=20)

    def __str__(self):
        return self.tag
