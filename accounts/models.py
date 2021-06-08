from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


class ReviewUser(AbstractBaseUser, PermissionsMixin):
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

    username_validator = UnicodeUsernameValidator()
    objects = UserManager()

    username = models.CharField(
        "username",
        max_length=50,
        blank=False,
        unique=True,
        help_text=(
            "Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
    )
    account_number = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
    )
    email = models.EmailField(unique=True, max_length=50)
    second_email = models.EmailField(unique=True, blank=True)
    bank = models.CharField(max_length=10, choices=BankChoices.choices)
    bank_number = models.CharField(max_length=20)

    comments = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
