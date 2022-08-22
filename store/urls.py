from rest_framework.routers import SimpleRouter
from .views import CategoryView, ProductView


router = SimpleRouter()

router.register('category', CategoryView)
router.register('product', ProductView)

