from django.views.generic import ListView

from .models import Product
# Create your views here.


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product_list.html'
