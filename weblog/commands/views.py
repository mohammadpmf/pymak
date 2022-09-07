from django.shortcuts import render

def show_commands(request):
    return render(request, 'commands/index.html')