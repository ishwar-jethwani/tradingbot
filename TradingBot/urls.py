from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .constants import ADMIN_SITE_HEADER

admin.site.site_header = ADMIN_SITE_HEADER

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="TradingBot API description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ishwarjethwaniillustration@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("swagger/",schema_view.with_ui(cache_timeout=0), name='schema-json'),
    path("redoc/",schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

# application urls
urlpatterns+=[
    path("accounts/",include("accounts.urls")),
    path("signals/",include("signals.urls")),
    path("trading/",include("activity.urls")),
    
]


