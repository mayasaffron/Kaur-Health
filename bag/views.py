from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products_and_services.models import Product, Service


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f' Updated {product.name} {service.name}'
                         'quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request,
                         f' {product.name} {service.name}'
                         ' added to your bag! ')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
