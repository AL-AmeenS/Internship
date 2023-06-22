from rest_framework import serializers
from .models import Customer, Product

class ProductSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_is_active(self, obj):
        return obj.is_active()

class CustomerSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'products']
