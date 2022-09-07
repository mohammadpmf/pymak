from django.shortcuts import render

def show_posts(request):
    return render(request, 'blog/index.html')