from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from asosiyapp.models import *
from userapp.models import *


# Create your views here.

class StatistikalarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            soz = request.GET.get("soz")
            if soz is None:
                stats = Statistika.objects.filter(sotuvchi__user=request.user)
            else:
                stats = Statistika.objects.filter(sotuvchi__user=request.user,mahsulot__nom__contains=soz)\
            |Statistika.objects.filter(sotuvchi__user=request.user,mijoz__ism__contains=soz)\
            |Statistika.objects.filter(sotuvchi__user=request.user,sotuvchi__ism__contains=soz)  \
            |Statistika.objects.filter(sotuvchi__user=request.user,mahsulot__brend__contains=soz)
            data = {
                'statistikalar': stats,
                'mahsulotlar': Mahsulot.objects.filter(sotuvchi__user=request.user),
                'mijozlar': Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'stats.html', data)
        else:
            return redirect("/")
    def post(self, request):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=request.POST.get("mahsulot"))
            if mahsulot.miqdor >= int(request.POST.get("miqdor")):
                Statistika.objects.create(
                mahsulot = Mahsulot.objects.get(id=request.POST.get("mahsulot")),
                mijoz = Mijoz.objects.get(id=request.POST.get("mijoz")),
                miqdor = request.POST.get("miqdor"),
                jami = request.POST.get("summa"),
                tolandi = request.POST.get("tolandi"),
                nasya = request.POST.get("nasiya"),
                sotuvchi = Sotuvchi.objects.get(user=request.user)
                )
                Mahsulot.objects.filter(id=request.POST.get("mahsulot")).update(
                    miqdor=(mahsulot.miqdor - int(request.POST.get("miqdor"))))

                Mijoz.objects.filter(id=request.POST.get("mijoz")).update(
                    qarz=Mijoz.objects.get(id=request.POST.get("mijoz")).qarz + int(request.POST.get("nasiya")))
            return redirect("/stats/")
        return redirect("/")

class StatsEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            data = {
                'stats': Statistika.objects.get(id=pk),
                'mahsulotlar': Mahsulot.objects.filter(sotuvchi__user=request.user),
                'mijozlar': Mijoz.objects.filter(sotuvchi__user=request.user)
            }
            return render(request, 'stats_update.html',data)

    def post(self, request, pk):
        if request.user.is_authenticated:
            mahsulot = Mahsulot.objects.get(id=request.POST.get("mahsulot"))
            if mahsulot.miqdor >= int(request.POST.get("miqdor")):
                Statistika.objects.filter(id=pk).update(
                mahsulot = Mahsulot.objects.get(id=request.POST.get("mahsulot")),
                mijoz = Mijoz.objects.get(id=request.POST.get("mijoz")),
                miqdor = request.POST.get("miqdor"),
                jami = request.POST.get("jami"),
                tolandi = request.POST.get("tolandi"),
                nasya = request.POST.get("nasiya"),
                )
                Mahsulot.objects.filter(id=request.POST.get("mahsulot")).update(
                    miqdor=(mahsulot.miqdor - int(request.POST.get("miqdor"))))

                Mijoz.objects.filter(id=request.POST.get("mijoz")).update(
                    qarz=Mijoz.objects.get(id=request.POST.get("mijoz")).qarz + int(request.POST.get("nasiya")))
            return redirect("/stats/")
        return redirect("/")

def StatsOchir(request, pk):
    if request.user.is_authenticated:
        Statistika.objects.get(id=pk).delete()
        return redirect("/stats/")
    return redirect("/")
def Logout(request):
    logout(request)
    return redirect("/")