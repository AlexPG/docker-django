from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import CreateProductForm
from .models import Product
# Create your views here.


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/product_list.html'


class ProductCreate(CreateView):
    form_class = CreateProductForm
    template_name = 'shop/product_create.html'
    success_url = reverse_lazy('shop:product_list')
