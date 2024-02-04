from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    author = models.CharField(max_length=40)

