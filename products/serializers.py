from rest_framework import serializers
from .models import Product
from accounts.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProductSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    like_count = serializers.IntegerField(source="like_users.count", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("author",)
