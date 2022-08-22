from rest_framework.routers import SimpleRouter
from .views import CategoryView, ProductView


app_name = "store"


router = SimpleRouter()
router.register(r'category', CategoryView)
router.register(r'product', ProductView)

urlpatterns = router.urls
