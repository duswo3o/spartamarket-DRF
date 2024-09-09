from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from django.core.paginator import Paginator

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
        page = request.GET.get("page", "1")
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 10)
        if int(page) <= paginator.num_pages:
            products = paginator.get_page(page)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {"detail": "존재하지 않는 페이지입니다"},
                status=status.HTTP_404_NOT_FOUND,
            )

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
            return Response("수정 권한이 없는 사용자입니다.")

    # 상품 삭제
    def delete(self, request, productID):
        product = get_object_or_404(Product, id=productID)
        writer = product.author
        if request.user == writer:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("삭제 권한이 없는 사용자입니다.")


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
