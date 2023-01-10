from django.shortcuts import render,redirect
from django.views import View
from .models import *
from userapp.models import *

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
            soz = request.GET.get("soz")
            if soz is None:
                mahsulotlar = Mahsulot.objects.filter(sotuvchi__user=request.user)
            else:
                mahsulotlar = Mahsulot.objects.filter(sotuvchi__user=request.user, sotuvchi__ism__contains=soz)|Mahsulot.objects.filter(
                    sotuvchi__user=request.user, nom__contains=soz)|Mahsulot.objects.filter(sotuvchi__user=request.user, nom__contains=soz)
            data = {
                'mahsulotlar': mahsulotlar
            }
            return render(request, 'products.html',data)
        else:
            return redirect("/")

    def post(self,request):
        if request.user.is_authenticated:
            Mahsulot.objects.create(
                nom = request.POST.get("pr_name"),
                brend = request.POST.get("pr_brand"),
                miqdor = request.POST.get("pr_amount"),
                narx = request.POST.get("pr_price"),
                olchov = request.POST.get("pr_olchov"),
                # kelgan_sana = request.POST.get("pr_name"),
                sotuvchi = Sotuvchi.objects.filter(user=request.user)[0]
            )
            return redirect("/bolimlar/mahsulotlar/")
        else:
            return redirect("/")

class MahsulotEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            data = {
                'product': Mahsulot.objects.get(id=pk)
            }
            return render(request, 'product_update.html',data)
        else:
            return redirect("/")

    def post(self,request,pk):
        if request.user.is_authenticated:
            sotuvchi = Sotuvchi.objects.get(user=request.user)
            mahsulot = Mahsulot.objects.get(id=pk)
            if mahsulot.sotuvchi == sotuvchi and request.user.is_staff:
                Mahsulot.objects.filter(id=pk).update(
                    nom = request.POST.get("pr_name"),
                    brend = request.POST.get("pr_brand"),
                    miqdor = request.POST.get("pr_amount"),
                    narx = request.POST.get("pr_price"),
                )
            return redirect("/bolimlar/mahsulotlar/")
        else:
            return redirect("/")
def MahsulotOchir(request, pk):
    if request.user.is_authenticated:
        sotuvchi = Sotuvchi.objects.get(user=request.user)
        mahsulot = Mahsulot.objects.get(id=pk)
        if mahsulot.sotuvchi == sotuvchi and request.user.is_staff:
            mahsulot.delete()
        return redirect("/bolimlar/mahsulotlar/")
    return redirect("/")


class MijozlarView(View):
    def get(self,request):
        if request.user.is_authenticated:
            soz = request.GET.get("soz")
            if soz is None:
                mijozlar = Mijoz.objects.filter(sotuvchi__user=request.user)
            else:
                mijozlar = Mijoz.objects.filter(sotuvchi__user=request.user, ism__contains=soz)|Mijoz.objects.filter(
                sotuvchi__user=request.user, nom__contains=soz)|Mijoz.objects.filter(sotuvchi__user=request.user, manzil__contains=soz)
            data = {
                # 'mijozlar': Mijoz.objects.all()
                'mijozlar': mijozlar
            }
            return render(request, 'clients.html', data)
        else:
            return redirect("/")

    def post(self,request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism = request.POST.get("client_name"),
                nom = request.POST.get("client_shop"),
                manzil = request.POST.get("client_address"),
                tel = request.POST.get("client_phone"),
                # qarz = request.POST.get("client_name"),
                sotuvchi = Sotuvchi.objects.get(user=request.user),
            )
            return redirect("/bolimlar/clientlar/")
        else:
            return redirect("/")

def ClientOchir(request, pk):
    if request.user.is_authenticated:
        sotuvchi = Sotuvchi.objects.get(user=request.user)
        client = Mijoz.objects.get(id=pk)
        if client.sotuvchi == sotuvchi and request.user.is_staff:
            Mijoz.objects.get(id=pk).delete()
        return redirect("/bolimlar/clientlar/")
    return redirect("/")


class ClientUpdateView(View):
    def get(self,request, pk):
        data = {
            'client': Mijoz.objects.get(id=pk)
        }
        return render(request, 'client_update.html',data)

    def post(self,request, pk):
        if request.user.is_authenticated:
            sotuvchi = Sotuvchi.objects.get(user=request.user)
            client = Mijoz.objects.get(id=pk)
            if client.sotuvchi == sotuvchi and request.user.is_staff:
                Mijoz.objects.filter(id=pk).update(
                    ism = request.POST.get("client_name"),
                    nom = request.POST.get("client_shop"),
                    manzil = request.POST.get("client_address"),
                    tel = request.POST.get("client_phone"),
                )
            return redirect("/bolimlar/clientlar/")
        return redirect("/")