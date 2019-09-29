from django.conf.urls import url, include
from ecomapp.views import base_view, category_view, product_view

urlpatterns = [
	url(r'^category/', base_view, name='base'),
    url(r'^$', base_view, name='base'),
]