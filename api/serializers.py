from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
	"""Maps the model instance to JSON format."""

	user = serializers.ReadOnlyField(source='user.username')

	class Meta:
		model = Item
		fields = ('id', 'name', 'completed', 'user', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')
