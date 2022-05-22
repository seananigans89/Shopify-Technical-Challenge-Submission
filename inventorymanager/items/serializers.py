from calendar import leapdays
from rest_framework import serializers
from items.models import Item

#Item Serializer

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'