from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserConfirmSerializer

User = get_user_model()


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserConfirmAPIView(generics.GenericAPIView):
    serializer_class = UserConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "User confirmed successfully"
        })


