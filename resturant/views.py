# authentication/views.py

from django.forms import EmailField
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth.models import User
from . models import Categorys, Products, Order, OrderItem
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

class FoodItemListView(APIView):
    def get(self, request):
        product_name = Products.objects.all()
        serializer = ProductSerializer(product_name, many=True)
        return Response(serializer.data)

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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem, Products  # Import your models
from .serializers import OrderSerializer  # Import your serializer

class OrderCreateView(APIView):
    def post(self, request):
        data = request.data

        # Create an order without associating it with a user
        order = Order.objects.create(total_price=0)

        # Process order items
        total_price = 0
        for item_data in data.get('order_items', []):
            product_name = Products.objects.get(pk=item_data['product_name'])
            quantity = item_data['quantity']
            total_price += product_name.price * quantity

            OrderItem.objects.create(order=order, product_name=product_name, quantity=quantity)

        # Update the total price
        order.total_price = total_price
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# from django.conf import settings
# from django.core.mail import EmailMessage
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class Sendmail(APIView):
#     def post(self, request):
#         email = request.data['too']
#         EmailMessage(
#                 'test email subject',
#                 'test email body,  this message is from python',
#                 settings.EMAIL_HOST_USER, 
#                 [email]
                
#         )
#         EmailMessage.send(self,fail_silently=False)
#         return Response({'status':True, 'message':'Email Sent Successfully'})
    
# views.py

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Order  # Import your Order model
# from .serializers import OrderSerializer  # Import your OrderSerializer
# from .utils import send_notification_email  # Import the email function

# class OrderCreateView(APIView):
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)

#         if serializer.is_valid():
#             # Create the order
#             order = serializer.save()

#             # Send an email notification
#             subject = 'New Order Created'
#             message = f'An order with ID {order.id} has been created.'
#             recipient_list = ['manojantony@gmail.com']  # Replace with the recipient's email address
#             send_notification_email(subject, message, recipient_list)

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
