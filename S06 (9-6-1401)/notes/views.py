from django.shortcuts import render

def show_notes(request):
    return render(request, 'notes/index.html')