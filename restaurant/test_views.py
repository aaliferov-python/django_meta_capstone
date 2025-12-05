from django.test import TestCase
from .views import MenuItemView

# TestCase class
class MenuItemViewTest(TestCase):
    def test_get_item(self):
        view = MenuItemView()
