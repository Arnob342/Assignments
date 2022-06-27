from django.db import models

# Create your models here.


class Selling(models.Model):
    pid = models.CharField(max_length=200)
    ItemName = models.CharField(max_length=300)
    perItemPrice = models.CharField(max_length=200)
    totalQuantity = models.CharField(max_length=50)


class Meta:
    db_table = "selling"
