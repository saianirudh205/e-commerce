# order/urls.py

from django.urls import path
from .views import OrderListCreateAPIView, OrderRetrieveAPIView

urlpatterns = [
    path('/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order-retrieve'),
]
