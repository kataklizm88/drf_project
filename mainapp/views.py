from django.shortcuts import render
from mainapp.models import Product, ProductCategory



def index(request):
    context = {'title': 'главная'}
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'products': Product.objects.all(),
        'categories':  ProductCategory.objects.all()
    }

    return render(request, 'mainapp/products.html', context)
