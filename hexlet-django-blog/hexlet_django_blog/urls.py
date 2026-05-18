"""
Конфигурация URL для проекта hexlet_django_blog.

Список `urlpatterns` направляет URL-адреса к представлениям. Для получения дополнительной информации см.:

https://docs.djangoproject.com/en/6.0/topics/http/urls/
Примеры:
Функциональные представления
1. Добавьте импорт: from my_app import views
2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Представления на основе классов

1. Добавьте импорт: from other_app.views import Home

2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение еще одной конфигурации URL

1. Импортируйте функцию include(): from django.urls import include, path

2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog.views import IndexView
from hexlet_django_blog import views

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("about/", views.about, name='about'),
    path('articles/', include('hexlet_django_blog.article.urls')),
    path('admin/', admin.site.urls),
]
