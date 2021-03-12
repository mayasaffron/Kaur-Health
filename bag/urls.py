from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add_product/<item_id>/',
         views.add_product_to_bag,
         name='add_product_to_bag'),
    path('adjust_product/<item_id>/',
         views.adjust_bag_product, name='adjust_bag_product'),
    path('remove/<item_id>/',
         views.remove_item, name='remove_item'),
]
