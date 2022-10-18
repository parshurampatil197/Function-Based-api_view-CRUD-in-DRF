from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from .models import Items
from .serializers import ItemSerializer


@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items = Items.objects.filter(**request.query_params.dict())
    else:
        items = Items.objects.all()

    if items:
        serializer = ItemSerializer(items, many=True)
        return Response({'message':'Success', 'data': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_items(request):
    serializer = ItemSerializer(data=request.data)

    if Items.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Item already Exist!!")

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message':'Success', 'data': serializer.data},status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['PUT'])
def update_items(request, pk):
    record = Items.objects.get(pk=pk)
    serializer = ItemSerializer(instance=record, data=request.data, partial=True)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'message':'Success', 'data': serializer.data},status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    record = get_object_or_404(Items, pk=pk)
    record.delete()
    return Response({'Message':'Success', 'data':'record deleted'}, status=status.HTTP_202_ACCEPTED)

