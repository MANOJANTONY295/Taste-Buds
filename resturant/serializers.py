# authentication/serializers.py

from rest_framework import serializers
from .models import CustomUser, Order, OrderItem

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'password', 'first_name', 'last_name')

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


from .models import Categorys, Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorys
        fields = ['id', 'category_name'] #,'category_description'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        #fields = '__all__'
        #fields = ['product_name_id', 'category_name_id', 'product_name', 'price', 'title', 'description', 'on_discount', 'discount_price', 'date_added']
        fields = ['id', 'product_name', 'category_name', 'price', 'offer', 'size', 'stock', 'description', 'on_discount', 'discount_price', 'date_added','image'] # 

# orders/serializers.py

# from rest_framework import serializers
# from .models import FoodItem, Order, OrderItem

# class FoodItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodItem
#         fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
