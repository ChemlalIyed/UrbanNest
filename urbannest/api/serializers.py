from rest_framework.serializers import ModelSerializer
from . import models

class ProductsSerializer(ModelSerializer):
    class Meta:
        model=models.Products
        fields="__all__"
class HomeSerializer(ModelSerializer):
    class Meta:
        model=models.Homepage_image
        fields="__all__"
class CartSerializer(ModelSerializer):
    class Meta:
        model=models.Cart
        fields="__all__"        
class OrdersSerializer(ModelSerializer):
    class Meta:
        model=models.Order
        fields="__all__" 
class UserSerializer(ModelSerializer):
    class Meta:
        model=models.User
        fields="__all__"        
class CategorysSerializer(ModelSerializer):
    class Meta:
        model=models.Category
        fields="__all__"  

class PhoneSerializer(ModelSerializer):
    class Meta:
        model=models.Phone
        fields="__all__"         