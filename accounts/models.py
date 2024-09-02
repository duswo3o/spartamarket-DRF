from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    username, 비밀번호, 이메일, 이름, 닉네임, 생일은 필수입력
    성별, 자기소개는 생각가능

    username과 이메일은 유일해야함
    """
    GENDER_CHOICES = [
        ("M", "남자"),
        ("W", "여자")
    ]

    # 장고에서 기본적으로 제공해주는 필드를 제거하기 위해 None으로 정의
    first_name = None
    last_name = None

    # 필수입력 필드
    email = models.EmailField("email_address", unique=True, blank=False)
    name = models.CharField("name", max_length=30)
    nickname = models.CharField("nickname", max_length=20)
    birthday = models.DateField("birthday")

    # 선택입력 필드
    gender = models.CharField("gender", max_length=1, choices=GENDER_CHOICES, blank=True)
    introduce = models.TextField("introduce", black=True)

