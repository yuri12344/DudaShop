from django.contrib import admin
from django.urls import path, include
from store.urls import router as store_router
from orders.urls import router as order_router


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('auth/',   include('rest_framework.urls')),
    path('api/v1/', include('cart.urls')),
    path('api/v1/', include(store_router.urls)),
    path('api/v1/', include(order_router.urls)),
    path('api/v1/', include(order_router.urls)),
     path("api/v1/", include("login.urls")),
    # path('api/v1/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
