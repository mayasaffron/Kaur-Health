from django.test import TestCase
from django.contrib.auth.models import User
from products_and_services.models import Product, Category


class TestProductView(TestCase):
    """
    Testing products and services views' renders templates
    for add and delete product functionality for superuser
    """
    def setUp(self):
        # Create author
        User.objects.create_superuser('superuser',
                                      'superuser@test.com',
                                      'superuserpassword')

        self.product = Product(name='test_name',
                               price=10,
                               description='test_description',
                               )
        self.product.save()

    def test_add_product(self):
        self.client.login(username='superuser', password='superuserpassword')
        response = self.client.get('/all_items/add/')
        self.assertTemplateUsed(response, 'products_and_services/add_product.html')

    def test_delete_product(self):
        self.client.login(username='superuser', password='superuserpassword')
        response = self.client.get('/all_items/delete/{0}/'
                                   .format(self.product.pk))
        self.assertRedirects(response, '/all_items/',
                             status_code=302, target_status_code=200,
                             fetch_redirect_response=True)
