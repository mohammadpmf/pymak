from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.samand1, name='ordinary'),
    path('lx/', views.samandlx, name='lx'),
    path('dena/', views.dena, name='dena'),
    path('denaplus/', views.denaplus,name='denaplus'),
]
