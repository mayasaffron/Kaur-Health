from django.urls import path
from .views import HomeView, BlogDetailView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='blog'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('new/', views.add_blog_post, name='add_blog_post'),
    path('update/<int:pk>/', views.update_blog,
         name='update_blog'),
    path('delete/<int:pk>/', views.delete_blog,
         name='delete_blog'),
]
