from django.shortcuts import render

def samand1(request):
    return render(request, 'samand/car1.html')

def samandlx(request):
    return render(request, 'samand/car2.html')

def dena(request):
    return render(request, 'samand/car3.html')

def denaplus(request):
    return render(request, 'samand/car4.html')
