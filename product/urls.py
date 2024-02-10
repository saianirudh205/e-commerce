# product/urls.py

from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-retrieve'),
]
