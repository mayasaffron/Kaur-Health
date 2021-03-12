from django import template
from products_and_services.models import Product

register = template.Library()
products = Product.objects.all()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
