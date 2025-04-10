from .models import CustomUser
from rest_framework import generics
from .seliarizers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
	queryset=CustomUser.objects.all()
	serializer_class = UserSerializer 
	permission_classes = [AllowAny]