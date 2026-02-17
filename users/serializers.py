from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserConfirmation

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=False)
        UserConfirmation.objects.create(user=user)
        return user

class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        username = attrs.get('username')
        code = attrs.get('code')
        try:
            user = User.objects.get(username=username)
            if user.confirmation.code != code:
                raise serializers.ValidationError("Invalid confirmation code")
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        attrs['user'] = user
        return attrs

    def save(self, **kwargs):
        user = self.validated_data['user']
        user.is_active = True
        user.save()
        user.confirmation.delete()
        return user
