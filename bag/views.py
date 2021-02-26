from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products_and_services.models import Product, Service


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_product_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f' Updated {product.name}'
                         f'quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request,
                         f' {product.name}'
                         ' added to your bag! ')

    request.session['bag'] = bag
    return redirect(redirect_url)


def add_service_to_bag(request, item_id):
    '''Add a quantity of the specified service to the shopping bag'''
    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f' Updated {service.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request,
                         f' {service.name} added to your bag! ')
    print(item_id)
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_product(request, item_id):
    '''Adjust the quantity of products the '''
    '''specified product to the shopping bag'''
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f' Updated {product.name}'
                         f' quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f' Removed {product.name} from your bag! ')
    print(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def adjust_bag_service(request, item_id):
    '''Adjust the quantity of the specified service to the shopping bag'''
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    service = get_object_or_404(Service, pk=item_id)

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f' Updated {service.name} quantity to'
                         f'{bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f' Removed {service.name} from your bag! ')
    print(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
