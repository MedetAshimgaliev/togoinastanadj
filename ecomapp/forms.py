# -*- coding: UTF-8 -*-
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password_check = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'password_check',
			'first_name',
			'last_name',
			'email'
		]

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = 'Login'
		self.fields['password'].label = 'Password'
		self.fields['password'].help_text = 'Set secure password'
		self.fields['password_check'].label = 'Re-type password'
		self.fields['first_name'].label = 'First name'
		self.fields['last_name'].label = 'Last name'
		self.fields['email'].label = 'Email'
		self.fields['email'].help_text = 'Please mention real e-mail address'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		password_check = self.cleaned_data['password_check']
		email = self.cleaned_data['email']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('That username already exists in the system!')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('That email address already exists in the system! Use another!')
		if password != password_check:
			raise forms.ValidationError('Passwords does not match. Try again!')

				


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