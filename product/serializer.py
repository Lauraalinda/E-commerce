from dataclasses import fields
from pyexpat import model
from product.models import Categories,Product,Cart,CartItem
from rest_framework import serializers

class Categoriesserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Categories
        fields=('category_Id','quantity','name','description')

class Productserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Product
        fields=('product_Id','category_Id','size','name','brand','image','quantity_in_stock',
                'color','price')

class Cartserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Cart
        fields=('cart_Id','user_id','number_of_products')

class CartItemserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CartItem
        fields=('cartItem_Id','name','cart_Id','quantity')































