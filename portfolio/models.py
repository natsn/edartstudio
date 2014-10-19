from django.db import models
from django.contrib.auth.models import User

class Art(models.Model):
    user = models.ForeignKey(User)
    art = models.FileField(upload_to='art')
    name = models.CharField(max_length=255) 
    rating = models.IntegerField(blank=True)

class Portfolio(models.Model):
    user = models.ForeignKey(User)
    arts = models.CommaSeparatedIntegerField(max_length=1000)
    about = models.TextField()
    rating = models.IntegerField(blank=True)

class Tag(models.Model):
	name = models.CharField(max_length=255)

class TagArt(models.Model):
	art = models.ForeignKey(Art)
	tag = models.ForeignKey(Tag)
