from Player.models import Player
from GameMap.models import Location
from Inventory.models import Item, ItemType
from rest_framework import serializers

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'user', 'name', 'email', 'playerclass', 'level', 'position')
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'locationId', 'description', 'locationType')

class InventoryTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemType
        fields = ('url', 'name')


class InventorySerializer(serializers.HyperlinkedModelSerializer):
  #  item_types = InventoryTypeSerializer(many=True, read_only=True)
    class Meta:
        model = Item
        fields = ('url', 'itemType', 'quality', 'owner')