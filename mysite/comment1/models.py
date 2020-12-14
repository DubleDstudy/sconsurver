from django.db import models

#Create your models here.

class Comment1(models.Model):
    uid = models.CharField(max_length=70, blank=True, default='')
    userid = models.CharField(max_length=70, blank=True, default='')
    comment = models.CharField(max_length=70, blank=True, default='')
    timestamp = models.CharField(max_length=70, blank=True, default='')

# Create your models here.
