from django.db import models
 
 
class User(models.Model):
    userid = models.CharField(max_length=70, blank=True, default='')
    name = models.CharField(max_length=70, blank=True, default='')
    passwd = models.CharField(max_length=70, blank=True, default='')
    usertype = models.CharField(max_length=70, blank=True, default='')
    score = models.IntegerField(blank=True, default=0)
# Create your models here.
