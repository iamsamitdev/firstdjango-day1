"""
URL configuration for firstdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views
from .todoListView import TodoListView

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('admin/', admin.site.urls),

    # path แบบมี parameter
    path('search/<str:keyword>/<int:page>', views.search, name='search'),

    # path แบบมี query string
    # http://localhost:8000/maps?type=satellite&lat=13.387378&lon=100.038930&z=17
    path('maps', views.maps, name='maps'),

    # API todo
    path('api/todos', TodoListView.as_view(), name='todos'),
]
