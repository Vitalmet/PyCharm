from django.views.generic import RedirectView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy

class IndexView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('article', kwargs={'tags': 'python', 'article_id': 42})

def about(request):
    return render(request, "about.html")