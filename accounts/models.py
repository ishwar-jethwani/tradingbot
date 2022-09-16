from email.policy import default
from sys import platform
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .manager import CustomUserManager
from .utils import *
from django.db.models.signals import pre_save

class User(AbstractBaseUser,PermissionsMixin):
    user_id         = models.CharField(max_length=10,unique=True,blank=True,null=True)
    username        = None
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    is_active       = models.BooleanField(('active'), default=True)
    email           = models.EmailField(('email address'),unique=True)
    date_joined     = models.DateTimeField(('date_joined'), auto_now_add=True)
    broker_platform = models.JSONField(default=dict,verbose_name="Broker Platforms",null=True)
    signal_platform = models.JSONField(default=dict,verbose_name="Signal Platforms",null=True)
    is_verified     = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')


def pre_save_create_user_id(sender, instance, *args, **kwargs):
    if not instance.user_id:
        instance.user_id= unique_user_id_generator(instance)


pre_save.connect(pre_save_create_user_id, sender=User)
