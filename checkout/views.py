from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('all_items'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IFjjIIPA0UV9eVp4bq'
                             'R4o9gSIiRfGDzBpzMvO3JC0oKyyKa3g'
                             'fDF34xcuIQCtRGwDIh5AAg2ms6i'
                             'M0Ny1O4cxxg00iwEX8n1h',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
