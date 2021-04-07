from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


def all_items(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    product_count = len(products.filter(service_category=False))
    service_count = len(products.filter(service_category=True))
    print(product_count, service_count)
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category']
            if categories == 'services':
                products = products.filter(service_category=True)
                categories = Category.objects.filter(name__in=categories)
                product_count = len(products.filter(service_category=False))
                service_count = len(products.filter(service_category=True))
            else:
                categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)
                product_count = len(products.filter(service_category=False))
                service_count = len(products.filter(service_category=True))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('all_items'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)

            products = products.filter(queries)

            product_count = len(products.filter(service_category=False))

            service_count = len(products.filter(service_category=True))

    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'product_count': product_count,
        'service_count': service_count,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products_and_services/all_items.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products_and_services/product_detail.html',
                  context)


@login_required
def add_product(request):
    '''A view to allow super users to add products'''
    if not request.user.is_superuser:
        messages.error(request, 'sorry only store owners can add products')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product not added, please recheck the form')
            return redirect(reverse('add_product'))
    else:
        form = ProductForm()

    template = 'products_and_services/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_product(request, product_id):
    '''A view to allow super users to edit products'''
    if not request.user.is_superuser:
        messages.error(request, 'sorry only store owners can update products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update, please recheck the form')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products_and_services/update_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    '''A view to allow super users to delete products'''
    if not request.user.is_superuser:
        messages.error(request, 'sorry only store owners can delete products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('all_items'))


def confirm_delete(request):
    """
   confirm delete
    """
    if request.method == 'POST':
        selected = request.POST.get('id-selected')
        product = get_object_or_404(Product, pk=selected)
        product.delete()
        messages.success(request, f'{product.name} has been deleted!')
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)
