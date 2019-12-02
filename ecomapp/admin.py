# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ecomapp.models import Category, Product, CartItem, Cart, Order

# Register your models here.

def make_payed(modeladmin, request, queryset):
	queryset.update(status='Paid')
make_payed.short_description = "Mark as paid"

class OrderAdmin(admin.ModelAdmin):
	list_filter = ['status']
	actions = [make_payed]



admin.site.register(Category)
# admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)