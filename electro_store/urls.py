"""
URL configuration for electro_store project.

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
from itertools import product

from django.contrib import admin
from django.urls import path, include
from category.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('category/', category_list, name='category_list'),  # create a list "Routing"=>> (app name, view name, name),
    path('category/', include('category.urls')),

    path('product/', include('product.urls')),
] + static(settings.MEDIA_URL,
           document_root = settings.MEDIA_ROOT) #take conf of media and revert it to list of urls
