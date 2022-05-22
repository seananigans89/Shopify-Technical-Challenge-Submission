from rest_framework import serializers
from ..models.item import Item
from ..models.shipment import Shipment


class ShipmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    itemList = ShipmentItemSerializer(many=True, required=False)
    class Meta:
        model = Shipment
        fields = '__all__'


class NewShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'