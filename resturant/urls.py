# authentication/urls.py

from django.urls import path
from .views import OrderCreateView, UserRegistrationAPIView, UserLoginAPIView, CategoryView, ProductListCreateAPIView#, Sendmail# ProductView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('categories/', CategoryView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='products-list-create'),
    #path('product/<int:pk>/', ProductListCreateAPIView.as_view(), name='product-detail'),
    #path('food-items/', ProductListCreateAPIView.as_view(), name='food-item-list'),#ProductView
    path('orders/', OrderCreateView.as_view(), name='order-create'),
    #path('api/send/mail', Sendmail.as_view()),
]
