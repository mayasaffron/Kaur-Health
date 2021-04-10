from django.test import TestCase
from products_and_services.models import Product, Category


class ProductTests(TestCase):
    """
    Test Product model returns product title
    """
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')


class CategoryNameTest(TestCase):
    """ Test Category model returns category friendly name """
    def test_string_representation(self):
        category = Category(name="test_category",
                            friendly_name="Test category")
        self.assertEqual(str(category.name), "test_category")
        self.assertEqual(str(category.friendly_name), "Test category")
