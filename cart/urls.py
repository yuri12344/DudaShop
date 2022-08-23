from rest_framework.routers import SimpleRouter
from .views import CategoryView, ProductView


router = SimpleRouter()

router.register('cart', CategoryView)
router.register('product', ProductView)

