from django.shortcuts import render
from .models import Article   # точка важна: .models

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})