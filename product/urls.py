from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView
)
from .views import ProductReviewListAPIView
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
)




urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:id>/', ProductDetailAPIView.as_view()),

    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:id>/', ReviewDetailAPIView.as_view()),
    path("api/v1/products/reviews/", ProductReviewListAPIView.as_view()),
     path("categories/", CategoryListCreateAPIView.as_view()),
    path("categories/<int:id>/", CategoryRetrieveUpdateDestroyAPIView.as_view()),

   
    path("products/", ProductListCreateAPIView.as_view()),
    path("products/<int:id>/", ProductRetrieveUpdateDestroyAPIView.as_view()),

  
    path("reviews/", ReviewListCreateAPIView.as_view()),
    path("reviews/<int:id>/", ReviewRetrieveUpdateDestroyAPIView.as_view()),
]
