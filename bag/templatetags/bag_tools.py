from django import template
from products_and_services.models import Product, Service

register = template.Library()
products = Product.objects.all()
services = Service.objects.all()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
