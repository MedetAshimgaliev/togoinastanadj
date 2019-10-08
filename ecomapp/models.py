# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
#from django.core.urlresolvers import reverse
from django.urls import reverse
from transliterate import translit

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(blank=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category_detail', kwargs={'category_slug':self.slug})

def pre_save_category_slug(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug = slugify(translit(unicode(instance.name), reversed=True))
		instance.slug = slug

pre_save.connect(pre_save_category_slug, sender=Category)


class Brand(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

def image_folder(instance, filename):
	filename = instance.slug + '.' +filename.split('.')[1]
	return "{0}/{1}".format(instance.slug, filename)

class ProductManager(models.Manager):

	def all(self, *args, **kwargs):
		return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
	#on_delete added x 2
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	brands = models.ForeignKey(Brand, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	description = models.TextField()
	image = models.ImageField(upload_to=image_folder)
	price = models.DecimalField(max_digits=9, decimal_places=4)
	available = models.BooleanField(default=True)
	objects = ProductManager()


	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'product_slug': self.slug})

class CartItem(models.Model):
	#on_delete added
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	qty = models.PositiveIntegerField(default=1)
	item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

	def __unicode__(self):
		return "Cart item product {0}".format(self.product.title)


class Cart(models.Model):

	items = models.ManyToManyField(CartItem, blank=True)
	cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

	def __unicode__(self):
		return str(self.id)

	def add_to_cart(self, product_slug):
		cart = self
		product = Product.objects.get(slug=product_slug)
		new_item, _ = CartItem.objects.get_or_create(product=product,item_total=product.price)
		if new_item not in cart.items.all():
			cart.items.add(new_item)
			cart.save()


	def remove_from_cart(self,product_slug):
		cart = self
		product = Product.objects.get(slug=product_slug)
		for cart_item in cart.items.all():
			if cart_item.product == product:
				cart.items.remove(cart_item)
				cart.save()
			