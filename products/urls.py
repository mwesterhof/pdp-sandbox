from django.urls import path

from .views import OrderProduct, ProductList, ProductDetail


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('<int:pk>/order/', OrderProduct.as_view(), name='product_order')
]
