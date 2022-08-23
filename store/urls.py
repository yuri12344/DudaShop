from email.mime import base
from rest_framework.routers import SimpleRouter
from .views import CategoryView, ProductView
from cart.views import CartView


router = SimpleRouter()

router.register('category', CategoryView)
router.register('product', ProductView)

