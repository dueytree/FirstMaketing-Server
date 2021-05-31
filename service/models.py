import re
from django.db import models
from django.conf import settings


class TimeStampedModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Recruit(TimeStampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recruit_post"
    )
    photo = models.ImageField(upload_to="service/recruit/%Y/%m/%d")
    product = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    celler = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ["-id"]


class Comment(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        ordering = ["-id"]
