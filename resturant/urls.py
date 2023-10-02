# authentication/urls.py

from django.urls import path
from .views import FoodorderView, CategoryView, ProductListCreateAPIView  # OrderCreateView,UserRegistrationAPIView, UserLoginAPIView, 
from resturant import views#, Sendmail# ProductView
from .views import register_user, user_login, user_logout

urlpatterns = [
    #path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    #path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('categories/', CategoryView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateAPIView.as_view(), name='products-list-create'),
    #path('product/<int:pk>/', ProductListCreateAPIView.as_view(), name='product-detail'),
    #path('food-items/', ProductListCreateAPIView.as_view(), name='food-item-list'),#ProductView
    path('orders/', FoodorderView.as_view(), name='order-create'),
    #path('api/send/mail', Sendmail.as_view()),
    path('subscribe/', views.subscribe, name='subscribe'),
    #path('api/order-food/', FoodOrderAPIView.as_view(), name='order-food'),


    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
