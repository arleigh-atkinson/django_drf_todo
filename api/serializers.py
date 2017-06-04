from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
	"""Maos the model instance to JSON format."""

	class Meta:
		model = Item
		fields = ('id', 'name', 'completed', 'date_created', 'date_modified')
		read_only_fields('date_created', 'date_modified')
