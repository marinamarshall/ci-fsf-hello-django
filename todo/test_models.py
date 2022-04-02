from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        """ test_done_defaults_to_false """
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.status)

    def test_item_string_method_returns_name(self):
        """ test_item_string_method_returns_name """
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')