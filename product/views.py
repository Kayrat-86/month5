from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from django.db.models import Avg
from .models import Product
from .serializers import ProductReviewSerializer
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer
)
from django.db.models import Count
from rest_framework import generics



class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategorySerializer
    lookup_field = 'id'


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.annotate(
            products_count=Count("products")
        )


class ProductReviewListAPIView(ListAPIView):
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        return Product.objects.annotate(
            rating=Avg("reviews__stars")
        )


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailAPIView(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailAPIView(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ReviewListAPIView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetailAPIView(APIView):
    def get(self, request, id):
        review = get_object_or_404(Review, id=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

