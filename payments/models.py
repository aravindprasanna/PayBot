from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CardProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    default_card = models.BooleanField(blank=True)
    card_no =  models.CharField(max_length=19,blank=True)
    expiration = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.card_no

class Biller(models.Model):
    biller_name = models.CharField(max_length=255,blank=False,unique=True)

class BillerProfile(models.Model):
    user = models.CharField(max_length=25)
    biller_name = models.CharField(max_length=25)
    biller_ref = models.CharField(max_length=10,blank=True)

class Transaction(models.Model):
    user = models.CharField(max_length=25)
    biller_name = models.CharField(max_length=25)
    biller_ref = models.CharField(max_length=10,blank=True)
    amount = models.FloatField(default=0,blank=False)
    status = models.BooleanField(default=False)