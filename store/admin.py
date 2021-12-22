from django.contrib import admin
from django.db.models import fields
from . import models

admin.site.site_header = 'Store Admin'
admin.site.index_title = 'Admin'

# Register your models here.

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'membership')
    # list_editable = ['last_name', 'membership']
    ordering = ['first_name', 'last_name']

@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['made_at', 'payment_method', 'customer']
    # fields = ['made_at', 'payment_method', 'customer']