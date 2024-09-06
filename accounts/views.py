from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

from .serializers import (
    UserSerializer,
    ProfileUpdateSerializer,
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.
class AccountAPIView(APIView):
    # 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    # 회원탈퇴
    @login_required
    def delete(self, request):
        user = get_user_model().objects.get(id=request.user.id)
        # 비밀번호 재입력 필요

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
