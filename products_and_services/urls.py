from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='all_items'),
    path('product_detail/<int:product_id>/',
         views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>/', views.update_product,
         name='update_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('delete/', views.confirm_delete,
         name='confirm_delete'),
]
