from django.test import TestCase
from .models import Item

class ModelTestCase(TestCase):
	"""Test suite for item model."""

	def setUp(self):
		self.item_name = 'Clean up kitchen.'
		self.item = Item(name=self.item_name, completed=False)

	def test_model_can_create_an_item(self):
		count = Item.objects.count()
		self.item.save()
		updated_count = Item.objects.count()
		self.assertEqual((count + 1), updated_count)
