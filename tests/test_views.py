from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from rest_framework.test import RequestsClient, APITestCase
from restaurant.models import Menu
from restaurant.views import *


class MenuViewTest(APITestCase):
    def setUp(self):
        item1 = Menu.objects.create(
            title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(
            title="Ribeye", price=100, inventory=100)
        item3 = Menu.objects.create(
            title="Salmon", price=90, inventory=100)

        self.sampleList = [item1, item2, item3]
        client = RequestsClient()

    def test_menu_item_count(self):
        self.assertEqual(Menu.objects.all().count(), 3)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        returnData = response.data
        dbMenuItems = MenuSerializer(self.sampleList, many=True).data

        self.assertEqual(returnData, dbMenuItems)
