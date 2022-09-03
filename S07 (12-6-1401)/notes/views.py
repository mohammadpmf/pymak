from django.shortcuts import render
from .models import Note2

def show_notes(request):
    notes = Note2.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'notes/index.html', context)  