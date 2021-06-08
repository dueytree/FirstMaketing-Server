from django.contrib.auth import get_user_model
from rest_framework import serializers

RecruitUser = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = RecruitUser.objects.create(
            username=validated_data["username"],
            email=self.validated_data["email"],
            second_email=self.validated_data["second_email"],
            gender=self.validated_data["gender"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = RecruitUser
        fields = ["pk", "username", "password", "email"]


class UserUpdateSerializer(serializers.Serializer):
    model = RecruitUser


class UserCommentSerializer(UserUpdateSerializer):
    comment = serializers.CharField(required=True)


class PasswordResetSerializer(UserUpdateSerializer):
    prev_password = serializers.CharField(
        required=True,
    )
    new_password = serializers.CharField(
        required=True,
    )
