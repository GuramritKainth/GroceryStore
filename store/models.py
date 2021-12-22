from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class GroceryItem(models.Model):
    title = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('R', 'Regular'),
        ('P', 'Premium'),
        ('N', 'Not a member')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='N')
    
    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
    
    class meta:
        ordering = ['last_name']

class Purchase(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('DC', 'Debit Card'),
        ('CC', 'Credit Card'),
        ('Ca', 'Cash')
    ]
    made_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=2, choices=PAYMENT_METHOD_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='purchases')
    def __str__(self) -> str:
        return str(self.made_at)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_items')
    grocery_item = models.ForeignKey(GroceryItem, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField()
     