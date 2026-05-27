from django.views.generic import RedirectView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy

class IndexView(RedirectView):
    permanent = False
    url = reverse_lazy('articles')

def about(request):
    return render(request, "about.html")