from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item

class CreateView(generics.ListCreateAPIView):
	"""Handles HTTP POST requests"""
	
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def perform_create(self, serializer):
		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""Handles HTTP GET, PUT, and DELETE requests"""

	queryset = Item.objects.all()
	serializer_class = ItemSerializer
