from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)

    post = models.Manager()

    def __str__(self):
        return self.title


class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.User.username} Profile'
