from django.shortcuts import render, get_object_or_404
from .models import Product, Service, Category


def all_items(request):
    products = Product.objects.all()
    services = Service.objects.all()

    context = {
        'products': products,
        'services': services,
    }
    return render(request, 'products_and_services/all_items.html', context)
