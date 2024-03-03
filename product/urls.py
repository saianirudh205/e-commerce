# product/urls.py

from django.urls import path
from .views import (
    ProductListCreateAPIView, ProductRetrieveAPIView, ProductAddToCartListCreateAPIView,
    ProductCartItemDetailAPIView)


urlpatterns = [
    path('/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
    path('/add_to_cart/', ProductAddToCartListCreateAPIView.as_view(), name='add_to_cart'),
    path('/cart_item/<int:pk>/', ProductCartItemDetailAPIView.as_view(), name='cart_item-detail'),
]
