from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artist(models.Model):
  name = models.CharField(max_length=255)
  origin = models.CharField(max_length=255)
  genre = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Album(models.Model):
  name = models.CharField(max_length=255)
  release_date = models.DateField()
  record_label = models.CharField(max_length=255)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albuns')

  def __str__(self):
    return self.name

class Song(models.Model):
  name = models.CharField(max_length=255)
  release_date = models.DateField()
  album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')

  def __str__(self):
    return self.name

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profiles')
  username = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=255)

  def __str__(self):
    return self.username

class Rate(models.Model):
  note = models.IntegerField()
  song = models.ForeignKey(Song, related_name='ratings', on_delete=models.CASCADE)
  comment = models.TextField(max_length=3000, null=True)
  profile = models.ForeignKey(Profile, related_name='ratings', on_delete=models.CASCADE)