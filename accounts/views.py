from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from django.contrib.auth.decorators import login_required

from .serializers import (
    UserSerializer,
    ProfileUpdateSerializer,
    UserDeleteSerializer,
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class AccountAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    # 회원탈퇴
    def delete(self, request):
        serializer = UserDeleteSerializer(data=request.data)
        if serializer.is_valid():
            if check_password(serializer.data.get("password"), request.user.password):
                request.user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response("비밀번호가 일치하지 않습니다.")
        else:
            return Response(serializer.errors)


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
            serializer = ProfileUpdateSerializer(
                instance=my_profile, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({"detail": "수정 권한이 없는 프로필입니다."})


class FollowView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, username):
        me = request.user
        you = get_object_or_404(get_user_model(), username=username)
        if me != you:
            if me in you.followers.all():
                you.followers.remove(me)
                return Response("unfollow", status=status.HTTP_200_OK)
            else:
                you.followers.add(me)
                return Response("follow", status=status.HTTP_200_OK)
