from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/health/', views.health_check, name='health_check'),
    path('api/auth/login/', views.auth_login, name='auth_login'),
    path('api/session/', views.api_session, name='api_session'),
    path('api/sync/', views.api_sync, name='api_sync'),
]

# Serve static files in both development and production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve pages directory as static files
urlpatterns += static('pages/', document_root=settings.BASE_DIR / 'pages')