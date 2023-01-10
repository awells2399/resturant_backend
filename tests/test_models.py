from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_add_menu_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")
