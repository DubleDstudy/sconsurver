from django.db import models

# Create your models here.
class Contents(models.Model):
    imageurl=models.CharField(max_length=70,blank=False, default='')
    uid=models.CharField(max_length=70,blank=True, default='')
    userid=models.CharField(max_length=70,blank=False, default='')
    timestamp=models.CharField(max_length=70,blank=False, default='')
    favoriteCount=models.IntegerField(blank=False, default=0)
    usertype=models.IntegerField(blank=False, default=0)
    explain=models.CharField(max_length=70,blank=True, default='')

