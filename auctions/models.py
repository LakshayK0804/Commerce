from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = [('Memes','Memes'),
                ('Processors','Processors'),
                ('Gpus', 'GPUS'),
                ('RAM','Ram'),
                ('Monitor','Monitor')]
    Category = models.CharField(max_length=255)
    Starting_Bid = models.IntegerField()
    Description = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + self.author + ' | ' + self.Category
