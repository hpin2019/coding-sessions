from django.db import models
# Create your models here.

class Quote(models.Model):
    text = models.CharField(max_length=200, blank=False, null=False)
    author = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.CharField(max_length=200,blank=True,null=True)
