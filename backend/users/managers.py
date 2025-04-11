from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):

    def create_user(self, password, username, **kwargs):

        # if user_type == 'regular' or user_type == 'superuser':
        #     if not username:
        #         raise ValueError("Users must have a username")
        #     else:
        #         if ' ' in username:
        #             raise ValidationError("Username mustn't contain spaces.")
        # else:
        #     username='username'
        #     user_type='regular'
        
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        print(user.is_superuser)
        if user.is_superuser:
            permissions = Permission.objects.filter(codename__in=['view_own_projects', 'add_new_project', 'del_own_project', 'view_all_projects', 'del_all_projects'])
        else :
            permissions = Permission.objects.filter(codename__in=['view_own_projects', 'add_new_project', 'del_own_project'])

        for permission in permissions:
            user.user_permissions.add(permission)

        return user
    
    def create_superuser(self, username, password, **kwargs):

        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        
        return self.create_user(username=username, password=password, **kwargs)