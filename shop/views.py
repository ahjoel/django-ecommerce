from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.db.models import Q
from cart.forms import CartAddProductForm


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "shop/index.html", context)


class ProductList(View):
    # model = Product
    # context_object_name = 'products'
    template_name = 'shop/product_list.html'

    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
        q = request.GET.get("q")
        if q:
            products = Product.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(category__name__icontains=q)
            )
        return render(request, self.template_name, {"products": products, "categories": categories})


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product_details.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["cart_product_form"] = CartAddProductForm
        return context