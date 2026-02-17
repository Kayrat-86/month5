from rest_framework import generics
from django.db.models import Count, Avg
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    ProductReviewSerializer
)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(
        products_count=Count('products')
    )
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(
        products_count=Count('products')
    )
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




class ProductReviewListAPIView(generics.ListAPIView):
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        return Product.objects.prefetch_related('reviews').annotate(
            rating=Avg('reviews__stars')
        )


