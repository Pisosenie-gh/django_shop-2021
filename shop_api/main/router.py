from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ProductViewSet, CategoryViewSet, CurrentUserView, UserAPIView
from ..cart.views import CartViewSet

main_router = SimpleRouter()

main_router.register('product', ProductViewSet, basename='product')
main_router.register('category', CategoryViewSet, basename='category')
main_router.register('cart', CartViewSet, basename='cart')

extra_urlpatterns = [
    path('check-user-is-authenticated/', CurrentUserView.as_view(), name='check-user-is-authenticated'),
    path('user/', UserAPIView.as_view())
]