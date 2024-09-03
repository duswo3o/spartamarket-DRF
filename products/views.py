from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    # 상품 목록 조회
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # 상품 등록
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    # 상품 수정
    def put(self, request, productID):
        product = get_object_or_404(Product, id=productID)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 상품 삭제
    def delete(self, request, productID):
        product = get_object_or_404(Product, id=productID)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

