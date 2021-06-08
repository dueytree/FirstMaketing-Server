from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)
from . import views


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="login"),
    path("password_reset/", views.PasswordReset.as_view(), name="password_reset"),
    path("user_update/", views.UserUpdate.as_view(), name="user_update"),
    path("user_comments/", views.UserComment.as_view(), name="user_comments"),
    path("token/", obtain_jwt_token),
    path("token/refresh/", refresh_jwt_token),
    path("token/verify/", verify_jwt_token),
]
