from django.contrib.auth.models import User
from rest_framework import serializers
from product.models import Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'created_at', 'created_by']