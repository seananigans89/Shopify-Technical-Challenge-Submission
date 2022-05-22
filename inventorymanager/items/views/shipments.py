from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.shipment import ShipmentSerializer, NewShipmentSerializer
from ..models.shipment import Shipment
from ..models.item import Item

class ShipmentsView(APIView):
    def post(self, request):
        shipment = NewShipmentSerializer(data=request.data)

        if not shipment.is_valid():
            return Response(shipment.errors, status=status.HTTP_400_BAD_REQUEST)

        shipment.save()
        newShipment = Shipment.objects.get(id = shipment.data['id'])
        retVal = ShipmentSerializer(newShipment)

        return Response(retVal.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        shipments = Shipment.objects.all()
        data = ShipmentSerializer(shipments, many=True).data
        return Response(data)

        