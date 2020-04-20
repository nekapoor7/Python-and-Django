from django.db import models

# Create your models here.

class Album(models.Model):
    article = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
       return self.name
