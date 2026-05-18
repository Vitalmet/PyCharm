from django.views import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        context = {
            'app_name': 'hexlet-django-blog',
            'description': 'Это приложение для статей блога'
        }
        return render(request, 'articles/index.html', context)