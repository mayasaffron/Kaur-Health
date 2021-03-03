from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add_product/<item_id>/',
         views.add_product_to_bag,
         name='add_product_to_bag'),
    path('add_service/<item_id>/',
         views.add_service_to_bag,
         name='add_service_to_bag'),
    path('adjust_product/<item_id>/',
         views.adjust_bag_product, name='adjust_bag_product'),
    path('adjust_service/<item_id>/',
         views.adjust_bag_service, name='adjust_bag_service'),
    path('remove/<item_id>/',
         views.remove_item, name='remove_item'),
]
