from rest_framework import serializers
from ..models.item import Item
from ..models.shipment import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    