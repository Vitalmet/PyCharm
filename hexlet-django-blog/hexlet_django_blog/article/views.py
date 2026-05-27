from django.views import View
from django.shortcuts import render

from hexlet_django_blog.article.models import Article

class IndexView(View):
    def get(self, request, *arrgs, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles
            },
        )
