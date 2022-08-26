from django.contrib import admin
from django.urls import path, include
from store.urls import router as store_router
from orders.urls import router as order_router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

admin.site.site_title = "DudaShop"
admin.site.site_header = "Bem vindo Painel Administrativo Dudashop"


from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[]
)

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('auth/',   include('rest_framework.urls')),
    path('api/v1/', include('cart.urls')),
    path('api/v1/', include(store_router.urls)),
    path('api/v1/', include(order_router.urls)),
    path('api/v1/', include(order_router.urls)),
    path("api/v1/", include("login.urls")),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
