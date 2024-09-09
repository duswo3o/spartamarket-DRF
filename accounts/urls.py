from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path("", views.AccountAPIView.as_view(), name="account"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("password/", views.ChangePasswordView.as_view(), name="change_password"),
    path("<str:username>/", views.Profile.as_view(), name="profile"),
    path("<str:username>/follow/", views.FollowView.as_view(), name="follow"),
]
