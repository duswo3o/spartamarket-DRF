from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("author",)

    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
