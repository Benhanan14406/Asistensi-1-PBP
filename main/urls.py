"""
URL configuration for asistensi1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='book_list'),
    path('add_book', add_book, name='add_book'),
path("json/books/", get_books_json, name="get_books_json"),
path("json/books/<int:book_id>/", get_book_json_by_id, name="get_book_json_by_id"),
]
