from django.urls import path
from .views import *


urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotView.as_view(), name='mahsulotlar'),
    path('clientlar/', MijozlarView.as_view(), name='mijozlar'),
]