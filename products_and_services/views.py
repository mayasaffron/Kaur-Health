from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Service, Category


def all_items(request):
    products = Product.objects.all()
    services = Service.objects.all()

    context = {
        'products': products,
        'services': services,
    }

    return render(request, 'products_and_services/all_items.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products_and_services/product_detail.html',
                  context)


def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }
    return render(request, 'products_and_services/service_detail.html',
                  context)
