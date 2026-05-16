from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {
        'app_name': 'hexlet-django-blog',
        'description': 'Это приложение для статей блога'
    }
    return render(request, 'articles/index.html', context)