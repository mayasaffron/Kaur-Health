from products_and_services.models import Product
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_product_to_bag(request, item_id):
    '''Add a quantity of the specified product to the shopping bag'''
    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    quantity = int(request.POST.get('quantity'))
    service = None
    if 'product_is_service' in request.POST:
        service = request.POST['product_is_service']
        bag = request.session.get('bag', {})
    if service:
        if item_id in list(bag.keys()):
            bag[item_id]['item_is_service'][product.name] += quantity
            messages.success(request, f' Updated {product.name}'
                             ' quantity to'
                             f' {bag[item_id]["item_is_service"][product.name]}!')

        else:
            bag[item_id] = {'item_is_service': {product.name: quantity}}
            messages.success(request, f'Added {product.name}'
                             ' to your bag! Please read the'
                             ' rules regarding services!')

    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f' Updated {product.name}'
                             f' quantity to {bag[item_id]} !')

        else:
            bag[item_id] = quantity
            messages.success(request, f' {product.name} added to your bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_product(request, item_id):
    '''Adjust the quantity of products the '''
    '''specified product to the shopping bag'''
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity in range(0, 1000):
        bag[item_id] = quantity
        messages.info(request, f'Updated {product.name}'
                      f' quantity to {bag[item_id]} !')
    else:
        bag.pop(item_id)
        messages.info(request, f'Removed {product.name} from your bag! ')
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
            messages.info(request, f'Removed service {product.name}'
                          ' from your bag!')
        else:
            bag.pop(item_id)
            messages.info(request, f'{product.name}'
                          ' deleted from your bag! ')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e} ')
        return HttpResponse(status=500)
