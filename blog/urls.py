from django.urls import path
from .views import HomeView, BlogDetailView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('detail/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', views.add_blog_post, name='add_blog_post'),
    path('update/<slug:slug>/', views.update_blog,
         name='update_blog'),
    path('delete/<int:pk>/', views.delete_blog,
         name='delete_blog'),
]
