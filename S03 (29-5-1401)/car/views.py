from django.shortcuts import render

def pride(request):
    return render(request, 'car/pride.html')

def pejo(request):
    return render(request, 'car/pejo.html')
