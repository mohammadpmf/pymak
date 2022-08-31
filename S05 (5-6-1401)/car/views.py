from django.shortcuts import render

def pride(request):
    context = {
        'name': 'Ali',
        'family': 'Ahmadi',
        'age': '39',
    }
    return render(request, 'car/pride.html', context=context)

def pejo(request):
    return render(request, 'car/pejo.html')
