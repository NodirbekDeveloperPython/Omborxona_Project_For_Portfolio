from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        u = authenticate(username = request.POST.get("login"),
                         password = request.POST.get('parol'))
        if u is None:
            return redirect('/')
        else:
            login(request, u)
            return redirect("/bolimlar/")


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")