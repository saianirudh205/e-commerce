# product/views.py
from rest_framework import generics
from rest_framework.views import APIView
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.response import Response


@permission_classes([IsAuthenticated])
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@permission_classes([IsAuthenticated])
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@permission_classes([IsAuthenticated])
class ProductAddToCartListCreateAPIView(APIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        try:
            my_object = CartItem.objects.get(product_id=product_id)
            my_object.quantity += quantity
            my_object.save()
        except:
            my_object = CartItem(product_id=product_id, quantity=quantity)
            my_object.save()

        # queryset = CartItem.objects.all()
        # serializer = CartItemSerializer

        serializer = CartItemSerializer(my_object)
        return Response(serializer.data)

    def get(self, request):
        queryset = CartItem.objects.all()

        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class ProductCartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
