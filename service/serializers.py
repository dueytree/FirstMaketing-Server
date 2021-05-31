from rest_framework import serializers
from .models import Recruit


class RecruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = [
            "id",
            "author",
            "created_at",
            "photo",
            "product",
            "location",
            "platform",
            "celler",
        ]
