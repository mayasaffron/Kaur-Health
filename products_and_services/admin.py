from django.contrib import admin
from .models import Category, Product, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'price',
        'product_image',
        'rating',
        )
    ordering = ('name', 'price')


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'category',
        'price',
        'product_image',
        'rating',
        )
    ordering = ('name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
