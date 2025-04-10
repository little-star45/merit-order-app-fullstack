from rest_framework import serializers
from .models import CustomUser

class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("style", {})
        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True
        super().__init__(*args, **kwargs)

class UserSerializer(serializers.ModelSerializer):
    password = PasswordField()

    class Meta:
        model = CustomUser
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
            user = CustomUser.objects.create_user(**validated_data)
            return user

