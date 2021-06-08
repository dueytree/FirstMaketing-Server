from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from .serializers import (
    PasswordResetSerializer,
    SignupSerializer,
    UserCommentSerializer,
    UserUpdateSerializer,
)


class SignupView(CreateAPIView):
    model = get_user_model()
    serializer_class = SignupSerializer


class PasswordReset(UpdateAPIView):
    model = get_user_model()
    serializer_class = PasswordResetSerializer

    def get_object(self):
        user = self.request.user
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(request.data)

        if serializer.is_vaild():
            if not user.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(UpdateAPIView):
    model = get_user_model()
    serializer_class = UserUpdateSerializer


class UserComment(UpdateAPIView):
    model = get_user_model()
    serializer_class = UserCommentSerializer

    def get_object(self):
        user = self.request.user
        return user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(request.data)

        if serializer.is_valid():
            comment = serializer.data.get("comment")
            if comment is None:
                raise ValidationError("Comment가 없습니다.")
            user.comments = comment
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
