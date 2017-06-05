from rest_framework import generics, permissions
from .permissions import IsUser
from .serializers import ItemSerializer
from .models import Item


class CreateView(generics.ListCreateAPIView):
    """Handles HTTP POST requests"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated, IsUser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles HTTP GET, PUT, and DELETE requests"""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated, IsUser)
