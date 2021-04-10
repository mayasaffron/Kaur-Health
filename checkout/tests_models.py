from django.test import TestCase
from checkout.models import Order, OrderLineItem
from products_and_services.models import Product


class OrderTests(TestCase):
    """
    Testing order line item total calculation
    """
    def test_subtotal_calculation(self):
        self.product = Product(name='test_name',
                               price=11,
                               description='test_description',
                               )
        self.product.save()
        self.order = Order(
            full_name="Test User",
            email="test_user@exampl.com",
            phone_number="12345",
            country="gb",
            postcode="e114dr",
            town_or_city="london",
            street_address1="40 test road",
            original_bag="",
            stripe_pid="",
        )
        self.order.save()
        self.order_line_item = OrderLineItem(
            order=self.order,
            product=self.product,
            quantity=2,

        )
        self.order_line_item.save()
        '''
        Testing product and order is created
        '''
        self.assertEqual(str(self.product.name), 'test_name')
        self.assertEqual(str(self.order.full_name), 'Test User')
        '''
        Testing order line item
        '''
        self.assertEqual(str(self.order_line_item.lineitem_total), '22')
        '''
        Testing order total
        '''
        self.assertEqual(str(self.order.order_total), '22')
