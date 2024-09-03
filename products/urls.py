from django.urls import path
from . import views


app_name = "products"
urlpatterns = [
    path("", views.ProductAPIView.as_view(), name="create")
]
