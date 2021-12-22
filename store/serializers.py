from django.db.models import fields
from rest_framework import serializers
from store import models
from store.models import Customer, GroceryItem, Purchase

class CustomerSerialzizer(serializers.ModelSerializer):
    purchases = serializers.StringRelatedField(many=True)    
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'membership', 'purchases']
        
class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        fields = ['id', 'title', 'unit_price', 'inventory']

class PurchaseSerialzier(serializers.ModelSerializer):
    # customer = serializers.StringRelatedField()
    class Meta:
        model = Purchase
        fields = ['id', 'customer', 'payment_method', 'made_at']