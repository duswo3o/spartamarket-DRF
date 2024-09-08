from rest_framework import serializers
from .models import Product, Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["tag"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("author",)

    like_count = serializers.IntegerField(source="like_users.count", read_only=True)
    tags = HashtagSerializer(many=True, read_only=True)
