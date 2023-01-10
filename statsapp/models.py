from django.db import models
from userapp.models import Sotuvchi
from asosiyapp.models import Mijoz, Mahsulot
# Create your models here.

class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField(default=1)
    jami = models.PositiveSmallIntegerField()
    tolandi = models.PositiveSmallIntegerField()
    nasya = models.PositiveSmallIntegerField(default=0)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.SET_NULL, null=True)