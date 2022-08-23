from django.contrib import admin
from django.urls import path, include
from store.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/cart', include('cart.urls')),
]
