from django.shortcuts import render
from rest_framework import generics
from .serializers import ItemSerializer
from .models import Item

class CreateView(generics.ListCreateAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

	def perform_create(self, serializer):
		serializer.save()
