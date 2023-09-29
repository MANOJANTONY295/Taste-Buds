# authentication/views.py

from django.forms import EmailField
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from . models import Categorys, Products, Order#, OrderItem
from . serializers import CategorySerializer, ProductSerializer, OrderSerializer
from rest_framework import permissions
from django.shortcuts import get_object_or_404

class UserRegistrationAPIView(APIView):
    def get(self, requet):
        data=CustomUser.objects.all()
        serializer = UserRegistrationSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UserLoginAPIView(APIView):
    def post(self, request):
        # Assuming 'username' and 'password' are included in the request data
        email = request.data.get('email')
        password = request.data.get('password')

        if email and password:
            # Perform any additional checks here if needed
            # For this example, we assume any username/password is valid

            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class CategoryView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        categories = Categorys.objects.all()
        if categories is None:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer =CategorySerializer(data=request.data)
        if serializer.is_valid():
            category_name = serializer.validated_data['category_name']
            if Categorys.objects.filter(category_name=category_name).exists():
                return Response({'message':'Category with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        if category is None:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        if category is None:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
from rest_framework.generics import ListCreateAPIView
from .models import Products  # Import your Product model
from .serializers import ProductSerializer
#class ProductView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        data = Products.objects.all()
        if data is None:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)
    
    # def post(self, request): #, format=None
    #     serializer =ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         product_name = serializer.validated_data['product_name']
    #         if product_name.objects.filter(product_name=product_name).exists():
    #             return Response({'message':'Product with this name already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        scrap_name = self.get_object(pk)
        if scrap_name is None:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(scrap_name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_name = self.get_object(pk)
        if product_name is None:
            return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        product_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# orders/views.py

class FoodorderView(APIView):
    def get(self, request):
        product_name = Order.objects.all()
        serializer = OrderSerializer(product_name, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# class OrderCreateView(APIView):
#     def post(self, request):
#         data = request.data
#         user = request.user  # Assuming authentication is required

#         # Create an order
#         order = Order.objects.create(user=user, total_price=0)

#         # Process order items
#         total_price = 0
#         for item_data in data.get('order_items', []):
#             product_name = Products.objects.get(pk=item_data['product_name'])
#             quantity = item_data['quantity']
#             total_price += product_name.price * quantity

#             OrderItem.objects.create(order=order, product_name=product_name, quantity=quantity)

#         # Update the total price
#         order.total_price = total_price
#         order.save()

#         serializer = OrderSerializer(order)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Order, OrderItem, Products  # Import your models
# from .serializers import OrderSerializer  # Import your serializer

# class OrderCreateView(APIView):
#     def post(self, request):
#         data = request.data

#         # Create an order without associating it with a user
#         order = Order.objects.create(total_price=0)

#         # Process order items
#         total_price = 0
#         for item_data in data.get('order_items', []):
#             product_name = Products.objects.get(pk=item_data['product_name'])
#             quantity = item_data['quantity']
#             total_price += product_name.price * quantity

#             OrderItem.objects.create(order=order, product_name=product_name, quantity=quantity)

#         # Update the total price
#         order.total_price = total_price
#         order.save()

#         serializer = OrderSerializer(order)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



#email sending
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm


def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Taste-Buds'
            message = 'Your Order Placed,Dear Customer,Thank you for choosing Taste Buds! We look forward to serving you soon! Sincerely,"Taste Buds" tastebuds@gmail.com'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'home.html', {'form': form})

#order food
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Products, Order, OrderItem
# from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer

# class FoodOrderAPIView(APIView):
#     def post(self, request, format=None):
#         # Retrieve data from the request (e.g., item IDs and quantities)
#         item_ids = request.data.get('item_ids', [])
#         quantity = request.data.get('quantity', [])

#         # Validate the request data
#         if not item_ids or not quantity:
#             return Response({'message': 'Item IDs and quantities are required.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Retrieve food items based on item IDs
#         product_name = Products.objects.filter(pk__in=item_ids)
#         if len(product_name) != len(item_ids):
#             return Response({'message': 'Invalid item IDs provided.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Calculate total price and create the order
#         total_price = sum(item.price * quantity for item, quantity in zip(product_name, quantity))
#         order = Order(total_price=total_price)
#         order.save()

#         # Create order items
#         order_items = []
#         for food_item, quantity in zip(product_name, quantity):
#             order_item = OrderItem(order=order, product_name=product_name, quantity=quantity)
#             order_items.append(order_item)
#         OrderItem.objects.bulk_create(order_items)

#         # Serialize and return the order details
#         serializer = OrderSerializer(order)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
