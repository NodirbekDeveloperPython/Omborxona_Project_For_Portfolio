from django.db import models
from userapp.models import Sotuvchi

# Create your models here.

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    miqdor = models.PositiveSmallIntegerField()
    narx = models.PositiveSmallIntegerField()
    olchov = models.CharField(max_length=50)
    kelgan_sana = models.DateField(auto_now_add=True)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.nom}, {self.brend}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    qarz = models.PositiveSmallIntegerField(default=0)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.ism}, {self.nom}({self.manzil})"