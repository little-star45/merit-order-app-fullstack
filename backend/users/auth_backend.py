from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class UserCustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        user = None

        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return None
        
        if user.check_password(password) and user.is_active:
            return user
        
        return None
