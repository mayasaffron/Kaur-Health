from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def anchor(all_items, products_section):
    return reverse(all_items) + '#' + products_section


@register.simple_tag
def anchor2(all_items, services_section):
    return reverse(all_items) + '#' + services_section
