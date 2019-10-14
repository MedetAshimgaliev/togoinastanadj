# -*- coding: UTF-8 -*-
from django import forms
from django.utils import timezone


class OrderForm(forms.Form):
	name = forms.CharField()
	last_name = forms.CharField(required=False)
	phone = forms.CharField()
	buying_type = forms.ChoiceField(widget=forms.Select(), choices = ([("self", "self"), ("delivery", "delivery")]))
	date = forms.DateField(widget=forms.SelectDateWidget(), initial = timezone.now())
	address = forms.CharField(required=False)
	comments = forms.CharField(widget=forms.Textarea, required=False)



	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Name'
		self.fields['last_name'].label = 'Last name'
		self.fields['phone'].label = 'Phone'
		self.fields['phone'].help_text = 'Please leave your real phone number'
		self.fields['buying_type'].label = 'Getting method'
		self.fields['address'].label = 'Address'
		self.fields['address'].help_text = 'Please mention region'
		self.fields['comments'].label = 'Comments'
		self.fields['date'].label = 'Delivery date'
		self.fields['date'].help_text = 'Delivery will be done in 24h.'