from django.test import TestCase, Client
from restaurant.models import MenuItem
from django.contrib.auth.models import User


class MenuViewTest(TestCase):

    def setUp(self):
        self.menu1 = MenuItem.objects.create(
            title="Grilled Steak", price=10, inventory=10
        )
        self.menu2 = MenuItem.objects.create(title="Pizza", price=7, inventory=100)

    def test_getall(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        client = Client()
        client.force_login(user)
        response = client.get("http://127.0.0.1:8000/restaurant/menu/")
        serialized_menus = 200
        self.assertEqual(response.status_code, serialized_menus)
