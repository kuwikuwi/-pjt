from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User  # 사용자 모델이 정의된 파일 경로를 넣어주세요
from .serializers import CustomRegisterSerializer  # 여기에는 해당 시리얼라이저 파일의 경로를 넣어주세요

class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        # 여기서는 간단히 첫 번째 사용자 데이터를 가져오도록 합니다.
        # 실제로는 세션, 토큰 또는 다른 인증 방식을 통해 현재 사용자를 식별하고 가져와야 합니다.
        user = User.objects.first()

        # 사용자 정보를 시리얼라이즈합니다.
        serializer = CustomRegisterSerializer(user)

        # 시리얼라이즈된 데이터를 반환합니다.
        return Response(serializer.data, status=status.HTTP_200_OK)