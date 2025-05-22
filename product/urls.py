from django.urls import path
from .views import *
from . import views


urlpatterns=[
    path('',Product_list.as_view(),name='product_list'),

    #path('', product_list, name='product_list'),
    #path('',Products_list.as_view(),name='product_list'),

    ##path('',views.product_list,name='product_list'),
    ##path('new/', product_new, name='product_new'),
    ##path('newF/', product_newF, name='product_newF'),
    ##path('update/<int:id>', product_update, name='product_update'),
    ##path('delete/<int:id>', views.product_delete, name='product_delete'),
    ##path('<int:id>',product_show_details, name='product_show_details'),
    ##path('updateF/<int:id>', views.product_updatef, name='product_updatef'),

]