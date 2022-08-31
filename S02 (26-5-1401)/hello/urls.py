from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_hello, name='show_hello'),
    path('amir/', views.show_amir, name='show_amir'),
]
