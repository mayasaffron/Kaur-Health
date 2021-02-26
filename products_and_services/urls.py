from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='all_items'),
    path('product_detail/<int:product_id>/',
         views.product_detail, name='product_detail'),
    path('service_detail/<int:service_id>/',
         views.service_detail, name='service_detail'),
]