from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormEditView,
    ArticleFormDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='articles'),    # список
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"), # редактирование
    path("<int:id>/", ArticleView.as_view(), name='article'), # просмотр
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"), # создание
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="articles_delete"), # удаление
]
