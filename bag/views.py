from products_and_services.models import Product
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


def view_bag(request):

    return render(request, 'bag/bag.html')
    print(request.session.get('bag', {}))


def add_product_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    service = bool(request.POST.get('product_is_service'))
    bag = request.session.get('bag', {})

    if service:
        if item_id in list(bag.keys()):
            if item_id in bag["services"]:
                bag["services"][item_id] += quantity
                messages.success(request, f' Updated service {product.name}'
                                 f'quantity to {bag[item_id]}'
                                 '[item_is_service"][service]!')
            else:
                bag[item_id]['product_is_service'][service] = quantity
                messages.success(request, f'added {product.name}'
                                 'to your bag! Please read the'
                                 'rules regarding services!')
        else:
            bag["services"] = {item_id: quantity}
            messages.success(request, f'added {product.name}'
                             'to your bag! Please read the'
                             'rules regarding services!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f' Updated {product.name}'
                             f'quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f' {product.name} added to your bag!')

    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)


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


def remove_item(request, item_id):
    ''' removes an item from the shopping bag '''
    product = get_object_or_404(Product, pk=item_id)

    try:
        service = None
        if 'product_is_service' in request.POST:
            service = request.POST['product_is_service']
        bag = request.session.get('bag', {})

        if service:
            del bag[item_id]['item_is_service'][service]
            if not bag[item_id]['item_is_service']:
                bag.pop(item_id)
            messages.success(request, f' Removed service {product.name}'
                             ' from your bag!')
        else:
            bag.pop(item_id)
            messages.success(request, f' {product.name}'
                             ' deleted from your bag! ')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'error removing item: {e} ')
        return HttpResponse(status=500)
