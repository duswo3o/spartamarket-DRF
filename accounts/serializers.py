from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = "__all__"

        exclude = (
            "followings",
            "groups",
            "user_permissions",
        )

        # response되는 데이터에서 password 데이터는 오지 않음
        # write_only : 인스턴스를 생성하거나 수정할 때만 사용
        extra_kwargs = {"password": {"write_only": True}}

    # serializer를 대상으로 save() 메서드를 호출하여 DB 인스턴스를 생성할 때의 동작 정의
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            # provide django, password will be hashing!
            instance.set_password(password)
        instance.save()
        return instance


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ("password",)

    def validate_username(self, attrs):
        username = get_user_model().objects.filter(username=attrs)
        if username.exists():
            raise serializers.ValidationError("이미 존재하는 아이디입니다.")
        return attrs

    def validate_email(self, attrs):
        email = get_user_model().objects.filter(email=attrs)
        if email.exists():
            raise serializers.ValidationError("이미 존재하는 이메일입니다.")
        return attrs


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["password"]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "password",
        ]
