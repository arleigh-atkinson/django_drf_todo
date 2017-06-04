from django.test import TestCase
from .models import Item
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

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

class ViewTestCase(TestCase):
	"""Test suite for API views."""

	def setUp(self):
		self.client = APIClient()
		self.item_data = { 'name': 'Take out trash', 'completed': True }
		self.response = self.client.post(
			reverse('create'),
			self.item_data,
			format='json')

	def test_api_can_create_an_item(self):
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_api_can_get_an_item(self):
		item = Item.objects.get()
		response = self.client.get(
			reverse('details', kwargs={'pk': item.id}),
			format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, item)
