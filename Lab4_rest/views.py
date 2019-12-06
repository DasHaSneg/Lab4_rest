from Inventory.models import Item, ItemType
from Player.models import Player
from GameMap.models import Location
from rest_framework import viewsets
from Lab4_rest.serializer import LocationSerializer, InventoryTypeSerializer, PlayerSerializer, InventorySerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class InventoryTypeViewSet(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = InventoryTypeSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = InventorySerializer
