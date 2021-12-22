import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Avg
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status
from .models import GroceryItem, Customer, Purchase
from .serializers import CustomerSerialzizer, GroceryItemSerializer, PurchaseSerialzier

# Create your views here.

# class based views
class GroceryItemList(APIView):
    def get(self, request):
        queryset = GroceryItem.objects.all()
        serializer = GroceryItemSerializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GroceryItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GroceryItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer
    lookup_field = 'id'

class PurchaseList(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialzier

class PurchaseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerialzier
    lookup_field = 'id'

# function based views
@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        query_set = Customer.objects.all()
        serializer = CustomerSerialzizer(query_set, many=True)
        return Response(serializer.data)
        # return render(request, 'store/customer.html', {'customers': list(query_set)})
    elif request.method == 'POST':
        serializer = CustomerSerialzizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, id):
    customer = get_object_or_404(Customer, pk=id)
    if request.method == 'GET':
        serializer = CustomerSerialzizer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerialzizer(customer, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def list_purchase(request):
    query_set = Purchase.objects.filter(customer__last_name__icontains='ad')
    # return HttpResponse('abc')
    return render(request, 'store/purchase.html', {'purchases': query_set})

def list_grocery_item(request):
    query_set = GroceryItem.objects.filter(inventory__lt=10)
    result = GroceryItem.objects.aggregate(count = Count('id'))
    return render(request, 'store/groceryitem.html', {'items': query_set, 'result': result})
