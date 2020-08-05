from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]
