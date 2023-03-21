from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string


def index(request):
    context = {'title': 'главная'}
    return render(request, 'mainapp/index.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    paginate_by = 3

    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'category_id' in kwargs.keys():
            self.object_list = Product.objects.filter(category_id=kwargs['category_id'])
        else:
            self.object_list = Product.objects.all()
        context = self.get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['page'] = None
        return self.render_to_response(context)




# def products(request, category_id=None, page=1):
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#     else:
#         products = Product.objects.all()
#
#     per_page = 3
#     paginator = Paginator(products.order_by('-price'), per_page)
#     products_paginator = paginator.page(page)
#     context = {'categories': ProductCategory.objects.all(), 'products': products_paginator}
#     if request.is_ajax():
#         context['page'] = 1
#         result = render_to_string('mainapp/product-paginate.html', context)
#         print('HELLO')
#         print(context)
#         print(JsonResponse({'result': result}))
#         return JsonResponse({'result': result})
#     return render(request, 'mainapp/products.html', context)



def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'categories':  ProductCategory.objects.all()
    }

    return render(request, 'mainapp/products.html', context)