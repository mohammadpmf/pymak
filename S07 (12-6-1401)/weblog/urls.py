from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.m_weblog, name='mohammad'),
    path('paniz/', views.p_weblog, name='paniz'),
]
