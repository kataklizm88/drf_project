from django.shortcuts import render
from mainapp.models import Product, ProductCategory

# Create your views here.

def index(request):
    context = {'title': 'главная'}
    return render(request, 'mainapp/index.html', context)

# def products(request):
#     context = {
#         'title': 'каталог',
#         'products': [
#             {
#                 'img': 'product-11',
#                 'name': 'Супер лампа',
#                 'description': 'Яркий свет.'
#             },
#             {
#                 'img': 'product-21',
#                 'name': 'Стул повышенного качества',
#                 'description': 'Не оторваться.'
#             },
#             {
#                 'img': 'product-31',
#                 'name': 'Настольный светильник',
#                 'description': 'Стильно.'
#             }
#
#         ]
#     }
#     return render(request, 'mainapp/products.html', context)
#
def products(request):
    context = {
        'products': Product.objects.all(),
        'categories':  ProductCategory.objects.all()
    }

    return render(request, 'mainapp/products.html', context)


