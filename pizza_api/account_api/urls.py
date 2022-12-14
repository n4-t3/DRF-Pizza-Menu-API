from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('register/',views.register_api, name='register_api'),
    path('user/',views.user_api, name='user_api'),
    path('order/',views.orders_api, name='orders_api'),
    path('order/<int:id>/',views.order_chosen, name='order_chosen'),
    path('cart/',views.cart_api, name='cart_api'),
    path('cart/<int:id>/',views.cart_chosen, name='cart_chosen'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
