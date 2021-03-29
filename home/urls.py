from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_form, name='contact'),
    path('thankyou/', views.contact_response, name='contact_response'),
]
