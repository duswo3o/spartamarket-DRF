from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class SignupAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class Profile(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, username):
        user_profile = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, username):
        # 현재 로그인한 사용자와 조회한 프로필이 같을 때만 수정 가능
        if request.user.username == username:
            my_profile = get_object_or_404(get_user_model(), username=username)
            serializer = UserSerializer(instance=my_profile, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
