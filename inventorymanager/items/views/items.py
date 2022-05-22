from ..models.item import Item
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers.item import ItemSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


class ItemsView(APIView):
    def get(self, request):
        items = Item.objects.filter(deleted=False)
        data = ItemSerializer(items, many=True).data
        return Response(data)

    def post(self, request):
        item = ItemSerializer(data=request.data)
        if not item.is_valid():
            return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)



class ItemView(APIView):

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if item.deleted:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data=ItemSerializer(item).data
        
        return Response(data)

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.deleted=True
        item.deletion_comment = request.data['deletion_comment']
        item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def patch(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if item.deleted:
            return Response(status=status.HTTP_404_NOT_FOUND)

        updated_item = ItemSerializer(item, data=request.data, partial=True)
        if updated_item.is_valid():
            updated_item.save()
            return Response(updated_item.data)
        return Response(updated_item.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemUndeleteView(APIView):
    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.deleted=False
        item.deletion_comment=None
        item.save()
        return Response(status=status.HTTP_200_OK)


class DeletedItemsView(APIView):
    def get(self, request):
        items = Item.objects.filter(deleted=True)
        data = ItemSerializer(items, many=True).data
        return Response(data)