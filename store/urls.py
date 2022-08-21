from rest_framework.routers import SimpleRouter
from .views import CategoryView


router = SimpleRouter()
router.register('category', CategoryView)
