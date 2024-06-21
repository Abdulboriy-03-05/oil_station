from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    name = models.CharField("Name", max_length=256)
    username = models.CharField("Username", max_length=256, unique=True,)
    number = models.IntegerField("Id raqami",null=True,blank=True)


    USERNAME_FIELD = "username"
    firts_name = None
    last_name = None

    def __str__(self):
        return f"{self.name} -- {self.username}"
    
    @property
    def avatar_url(self):
        return f"{settings.HOST}{self.avatar.url}" if self.avatar else ""


    class Meta:
        db_table ="user"
        verbose_name = "user"
        verbose_name_plural = "users"