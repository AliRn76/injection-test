from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    username = models.CharField(max_length=120, unique=True)
    password = models.CharField(max_length=200)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    class Meta:
        db_table = 'user'

    def __str__(self) -> str:
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

class Credit(models.Model):
    channel_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'credit'

