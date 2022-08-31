from django.urls import path, include
from . import views


urlpatterns = [
    path('pride/', views.pride, name='pride'),
    path('pejo/', views.pejo, name='pejo'),
    path('samand/', include('samand.urls')),
]
