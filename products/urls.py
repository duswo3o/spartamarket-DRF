from django.urls import path
from . import views


app_name = "products"
urlpatterns = [
    path("", views.ProductAPIView.as_view(), name="product"),
    path("<int:productID>/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]
