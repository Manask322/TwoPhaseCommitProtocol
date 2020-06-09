from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False)
    port = models.IntegerField(null=False)
    amount = models.IntegerField(null=False,default=200)

class Status(models.Model):
    site = models.OneToOneField(Site,on_delete=models.CASCADE)
    status = models.IntegerField(null=False)