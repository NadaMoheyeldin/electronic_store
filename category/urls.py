from django.urls import path
from .views import *

urlpatterns = [
    path('', category_list, name='category_list'),  # create a list "Routing"=>> (app name, view name, name),
    path('add/', category_add, name='category_add'),
    path('update/<int:id>', category_update, name='category_update'),
    # <> is a variable with a primitive data type

]
