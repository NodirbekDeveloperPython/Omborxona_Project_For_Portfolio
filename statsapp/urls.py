from django.urls import path
from .views import *

urlpatterns = [
    path('', StatistikalarView.as_view()),
    path('stats_edit/<int:pk>/', StatsEditView.as_view(), name='stats_edit'),
    path('stats_ochir/<int:pk>/', StatsOchir),
    path('logout/', Logout, name='logout'),
]