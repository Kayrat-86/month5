from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView,
    ProductReviewListAPIView
)

urlpatterns = [
   
    path("categories/", CategoryListCreateAPIView.as_view()),
    path("categories/<int:id>/", CategoryRetrieveUpdateDestroyAPIView.as_view()),

    
    path("products/", ProductListCreateAPIView.as_view()),
    path("products/<int:id>/", ProductRetrieveUpdateDestroyAPIView.as_view()),

    
    path("reviews/", ReviewListCreateAPIView.as_view()),
    path("reviews/<int:id>/", ReviewRetrieveUpdateDestroyAPIView.as_view()),

   
    path("products/reviews/", ProductReviewListAPIView.as_view()),
]

