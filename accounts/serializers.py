from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        exclude = (
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
        extra_kwargs = {
            "username": {
                "required": True,
            },
            "email": {
                "required": True,
            },
        }

    def validate_username(self, attrs):
        username = get_user_model().objects.filter(username=attrs)
        if username.exists():
            raise serializers.ValidationError("이미 존재하는 아이디입니다.")
        return attrs

    def validate_email(self, value):
        user = self.context
        email = get_user_model().objects.filter(email=value)
        if email.exists():
            raise serializers.ValidationError("이미 존재하는 이메일입니다.")
        return value


class ChangePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ["new_password", "confirm_password", "old_password"]

    def validate(self, attrs):
        # 변경 패스워드 확인 절차
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "패스워드가 일치하지 않습니다"}
            )

        # 기존 패스워드와 변경할 패스워드는 상이해야 함
        if attrs["new_password"] == attrs["old_password"]:
            raise serializers.ValidationError(
                {"password": "기존 패스워드와 동일합니다."}
            )

        return attrs

    # 기존 비밀번호를 맞게 입력하였는지 검사
    def validate_old_password(self, value):
        me = self.context
        if not me.check_password(value):
            raise serializers.ValidationError("기존 패스워드가 일치하지 않습니다.")
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data["new_password"])
        instance.save()

        return instance


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "password",
        ]
