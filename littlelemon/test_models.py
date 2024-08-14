from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price="5", inventory=50)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream : 5")
