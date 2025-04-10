from django.db import models

from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # class UserType(models.TextChoices):
    #     REGULAR = 'regular', _('Regular User')
    #     SUPER = 'super', _('Superuser')

    username = models.CharField(max_length=40, unique=True)
    # user_type = models.CharField(max_length=10, choices=UserType.choices, default=UserType.REGULAR)
    # email = models.EmailField(unique=True, blank=True, null=True)

    # @property
    # def USERNAME_FIELD(self):
    #     if self.user_type == self.UserType.SUPER:
    #         return 'email'
    #     return 'username'

    USERNAME_FIELD = 'username'

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()    
    
    def __str__(self) -> str:
        return self.username or "No user in database"