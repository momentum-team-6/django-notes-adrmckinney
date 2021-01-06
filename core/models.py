from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title