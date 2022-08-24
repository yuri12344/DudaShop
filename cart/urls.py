from .views import CartView
from django.urls import path


urlpatterns = [
    path('cart/', CartView.as_view(), name='cart_detail'),
    path('cart/<int:product_id>', CartView.as_view(), name='cart_add_update_or_update'),
]
