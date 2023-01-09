from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    user = models.ManyToManyField(User, null=True)
    vazifa = models.CharField(max_length=50, blank=True)
    def __str__(self): return f"{self.ism}, {self.nom}({self.manzil})"

