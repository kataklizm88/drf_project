from django.urls import path
from mainapp.views import products

app_name = 'mainapp'

# urlpatterns = [
#     path('', views.ProductListView.as_view(), name="index"),
#     path('<int:category_id>/', views.ProductListView.as_view(), name='product'),
#     # path('page/<int:page>/', views.ProductListView.as_view(), name='page')
#     path('page/<int:page>/', views.products, name='page')
# ]

urlpatterns = [
    path('', products, name="index"),
    path('<int:category_id>/', products, name='product')
]

