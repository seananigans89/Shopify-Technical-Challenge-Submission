from ..models.item import Item
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers.item import ItemSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


class ItemsView(APIView):
    def get(self, request):
        items = Item.objects.all()
        data = ItemSerializer(items, many=True).data
        return Response(data)




class ItemView(APIView):
    def post(self, request):
        item = ItemSerializer(data=request.data)
        if not item.is_valid():
            return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        data=ItemSerializer(item).data
        return Response(data)

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        updated_item = ItemSerializer(item, data=request.data, partial=True)
        if updated_item.is_valid():
            updated_item.save()
            return Response(updated_item.data)
        return Response(updated_item.errors, status=status.HTTP_400_BAD_REQUEST)