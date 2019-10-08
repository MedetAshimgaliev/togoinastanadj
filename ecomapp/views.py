# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
#from django.core.urlresolvers import reverse 
from django.urls import reverse
from ecomapp.models import Category, Product, CartItem, Cart
from decimal import Decimal

# Create your views here.


def base_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	categories = Category.objects.all()
	products = Product.objects.all()
	context = {
		'categories': categories,
		'products': products,
		'cart': cart
	}
	return render(request, 'base.html', context)

def product_view(request,product_slug):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	product = Product.objects.get(slug=product_slug)
	context = {
		'product': product,
		'cart': cart
	}
	return render(request, 'product.html', context)

def category_view(request,category_slug):
	category = Category.objects.get(slug=category_slug)
	products_of_category = Product.objects.filter(category=category)
	context = {
		'category': category,
		'products_of_category': products_of_category
	}
	return render(request, 'category.html', context)


def cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	context = {
		'cart':cart
	}
	return render(request, 'cart.html', context)

def add_to_cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	cart.add_to_cart(product.slug)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	return JsonResponse({ 'cart_total': cart.items.count(),'cart_total_price':cart.cart_total })


def remove_from_cart_view(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	cart.remove_from_cart(product_slug)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	return JsonResponse({ 'cart_total': cart.items.count(),'cart_total_price':cart.cart_total })
	
def change_item_qty(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)
	qty = request.GET.get('qty')
	item_id = request.GET.get('item_id')
	cart_item = CartItem.objects.get(id=int(item_id))
	cart_item.qty = int(qty)
	cart_item.total = int(qty) * Decimal(cart_item.product.price)
	cart_item.save()
	print(qty)
	print(cart_item.total)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	#return JsonResponse({'cart_total':cart.items.count(), 'item_total': cart_item.item_total }) 
	return JsonResponse(
		{ 'cart_total': cart_item.qty,
		  'item_total':cart_item.total,
		  'cart_total_price':cart.cart_total
		  })