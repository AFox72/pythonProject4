from django.contrib.auth.models import User
from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    hair_type = models.CharField(max_length=20)


    owner = models.ForeignKey(User, on_delete=models.CASCADE)