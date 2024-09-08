from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,  # GET은 인증이 필요없고 POST, PUT, DELETE 요청은 인증이 필요함
    ]

    # 상품 목록 조회
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # 상품 등록
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,  # GET은 인증이 필요없고 POST, PUT, DELETE 요청은 인증이 필요함
    ]

    # 상품 수정
    def put(self, request, productID):
        product = get_object_or_404(Product, id=productID)
        writer = product.author
        if request.user == writer:
            serializer = ProductSerializer(
                instance=product, data=request.data, partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response("수정 권한이 업는 사용자입니다.")

    # 상품 삭제
    def delete(self, request, productID):
        product = get_object_or_404(Product, id=productID)
        writer = product.author
        if request.user == writer:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("삭제 권한이 업는 사용자입니다.")


class ProductLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, productID):
        product = get_object_or_404(Product, id=productID)
        user = get_user_model().objects.get(id=request.user.id)

        if user in product.like_users.all():
            product.like_users.remove(user)
            return Response("unlike", status=status.HTTP_200_OK)
        else:
            product.like_users.add(user)
            return Response("like", status=status.HTTP_200_OK)
