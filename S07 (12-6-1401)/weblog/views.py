from django.shortcuts import render

def m_weblog(request):
    return render(request, 'weblog/m_weblog.html')

def p_weblog(request):
    context = {
        'first': 'salam',
        'second': 'bye'
    }
    return render(request, 'weblog/p_weblog.html', context)
