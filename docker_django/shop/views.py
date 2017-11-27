from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class ProductList(TemplateView):
    template_name = 'shop/product_list.html'
