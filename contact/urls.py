from django.urls import path
from . import views


urlpatterns = [
    path('', views.contactform, name='contactform'),
    path('contact_response/', views.contact_response, name='contact_response'),
]
