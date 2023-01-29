from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('auth/', include("djoser.urls")),
    path(r'auth/', include('djoser.urls.jwt')),
    path("api/", include("users.urls")),
    path("api/", include("ads.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema')),
    path("api/token/", TokenObtainPairView.as_view(), name="Obtain"),
    path("api/refresh/", TokenRefreshView.as_view(), name="Refresh"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
