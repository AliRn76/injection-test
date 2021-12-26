from django.contrib.auth.backends import BaseBackend
from .models import User
from django.utils.module_loading import import_string

def load_backend(path):
    return import_string(path)()

class UsernameBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
