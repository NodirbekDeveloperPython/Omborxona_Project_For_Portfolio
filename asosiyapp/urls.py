from django.urls import path
from .views import *


urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotView.as_view(), name='mahsulotlar'),
    path('mahsulot_ochir/<int:pk>/', MahsulotOchir),
    path('clientlar/', MijozlarView.as_view(), name='mijozlar'),
    path('client_ochir/<int:pk>/', ClientOchir),
    path('client_edit/<int:pk>/', ClientUpdateView.as_view()),
]