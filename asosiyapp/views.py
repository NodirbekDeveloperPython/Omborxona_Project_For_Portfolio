from django.shortcuts import render,redirect
from django.views import View
from .models import *


# Create your views here.

class BolimlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect("/")


class MahsulotView(View):
    def get(self,request):
        if request.user.is_authenticated:
            data = {
                'mahsulotlar': Mahsulot.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'products.html',data)
        else:
            return redirect("/")

class MijozlarView(View):
    def get(self,request):
        if request.user.is_authenticated:
            data = {
                # 'mijozlar': Mijoz.objects.all()
                'mijozlar': Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'clients.html', data)
        else:
            return redirect("/")