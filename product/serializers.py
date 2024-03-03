from rest_framework import serializers
from .models import Category, Product, CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'image_url', 'category_id', 'category_name']

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.CharField(source='product.price', read_only=True)
    product_created_date = serializers.CharField(source='product.created_date', read_only=True)
    product_updated_date = serializers.CharField(source='product.updated_date', read_only=True)
    class Meta:
        model = CartItem
        fields = [
            'id', 'product', 'quantity', 'product_id', 
            'product_name', 'product_price', 'created_date',
            'updated_date', 'product_created_date', 'product_updated_date']