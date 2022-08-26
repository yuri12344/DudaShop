from rest_framework.routers import SimpleRouter
from .views import OrderViewSet



router = SimpleRouter()

router.register('order', OrderViewSet)

urlpatterns = router.urls 