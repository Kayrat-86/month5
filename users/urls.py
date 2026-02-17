from django.urls import path
from .views import UserRegisterAPIView, UserConfirmAPIView

urlpatterns = [
    path('users/register/', UserRegisterAPIView.as_view()),
    path('users/confirm/', UserConfirmAPIView.as_view()),
]

