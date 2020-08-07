from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.urls import reverse
Categories_Available = [('Memes','Memes'),
                        ('Processors','Processors'),
                        ('Gpus', 'GPUS'),
                        ('RAM','Ram'),
                        ('Monitor','Monitor')]
class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.CharField(choices=Categories_Available, max_length=10)
    Starting_Bid = models.IntegerField()
    Description = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + self.Category

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id)))
