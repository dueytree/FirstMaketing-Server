from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    class BankChoices(models.TextChoices):
        하나 = "하나은행"
        신한 = "신한은행"
        국민 = "국민은행"
        우리 = "우리은행"
        농협 = "농협은행"
        카카오 = "카카오뱅크"

    full_name = models.CharField(max_length=20)
    avatar = models.ImageField(
        blank=True,
        upload_to="accounts/avatar/%Y/%m/%d",
        help_text="png/jpg 파일을 업로드 해주세요.",
    )
    account_number = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    email = models.EmailField(unique=True)
    second_email = models.EmailField(unique=True)
    bank = models.CharField(max_length=10, choices=BankChoices.choices)
    bank_number = models.CharField(max_length=20)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image", self.username)  # TODO: username?
