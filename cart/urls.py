from .views import CartView
from django.urls import path


urlpatterns = [
    path('/', CartView.as_view(), name='cart_detail'),
    path('/<int:product_id>', CartView.as_view(), name='cart_add_update_or_update'),
]
