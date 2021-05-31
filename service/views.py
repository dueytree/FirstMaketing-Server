from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Recruit
from .serializers import RecruitSerializer


class PostViewSet(ModelViewSet):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer

    # from rest_framework.permissions import AllowAny
    # permission_classes = [AllowAny] # FIXME: 인증 적용, 미사용
