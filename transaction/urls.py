# transaction/urls.py

from django.urls import path
from .views import TransactionListCreateAPIView, TransactionRetrieveAPIView

urlpatterns = [
    path('/', TransactionListCreateAPIView.as_view(),
         name='transaction-list-create'),
    path('/<int:pk>/', TransactionRetrieveAPIView.as_view(),
         name='transaction-retrieve'),
]
