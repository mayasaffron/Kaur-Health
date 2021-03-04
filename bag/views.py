from products_and_services.models import Product, Service
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


def view_bag(request):
    product = Product.objects.all()
    service = Service.objects.all()
    context = {
        'product': product,
        'service': service,
    }

    return render(request, 'bag/bag.html', context)
    print(request.session.get('bag', {}))


def add_product_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.info(request,
                      f' Updated {product.name}'
                      f'quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request,
                         f' {product.name}'
                         ' added to your bag! ')

    request.session['bag'] = bag
    return redirect(redirect_url)
    print("PRINTING BAG (product)")
    print(request.session.get('bag', {}))


def add_service_to_bag(request, item_id):
    '''Add a quantity of the specified service to the shopping bag'''
    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.info(request,
                         f' Updated {service.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request,
                         f' {service.name} added to your bag! ')
    print(item_id)
    request.session['bag'] = bag
    return redirect(redirect_url)
    print("PRINTING BAG(service)")
    print(request.session.get('bag', {}))


def adjust_bag_product(request, item_id):
    '''Adjust the quantity of products the '''
    '''specified product to the shopping bag'''
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0:
        bag[item_id] = quantity
        messages.info(request, f' Updated {product.name}'
                               f' quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.warning(request, f' Removed {product.name} from your bag! ')
    print("working? item_id")
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def adjust_bag_service(request, item_id):
    '''Adjust the quantity of the specified service to the shopping bag'''
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    service = get_object_or_404(Service, pk=item_id)

    if quantity > 0:
        bag[item_id] = quantity
        messages.info(request, f' Updated {service.name} quantity to '
                      f'{bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.warning(request, f' Removed {service.name} from your bag! ')
    print(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, item_id):
    '''Remove item from shopping bag'''
    bag = request.session.get('bag', {})
    try:
        bag.pop(item_id)
        messages.success(request, ' Removed item from your bag!')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f' Error removing item: (e) ')
        return HttpResponse(status=500)
