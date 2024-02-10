# ecommerce_project/urls.py

# customer/urls.py

from django.urls import path
from .views import CustomerListCreateAPIView, CustomerRetrieveAPIView

urlpatterns = [
    path('/', CustomerListCreateAPIView.as_view(),
         name='customer-list-create'),
    path('/<int:pk>/', CustomerRetrieveAPIView.as_view(),
         name='customer-retrieve'),
]
