from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Post(models.Model) :
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200)
    seller = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField()
    years = models.IntegerField(default=0)
    months = models.IntegerField(default=0)
    days = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    phone = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    wallet = models.IntegerField(default=5000)

    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) :
        # self.published_date = timezone.now()
        self.save()

    def __str__(self) :
        return self.author


class UserProfile(models.Model) :
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    wallet = models.IntegerField(default=5000)

    def __str__(self) :
        return self.user.username

