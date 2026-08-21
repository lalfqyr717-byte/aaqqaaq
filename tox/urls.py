from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.pages_redirect, name='index_redirect'),
    path('admin/', admin.site.urls),
    path('api/health/', views.health_check, name='health_check'),
    path('api/auth/login/', views.auth_login, name='auth_login'),
    path('api/session/', views.api_session, name='api_session'),
    path('api/sync/', views.api_sync, name='api_sync'),
    # Redirect all pages requests to home since pages directory is empty
    re_path(r'^pages/(?P<path>.*)$', views.pages_redirect, name='pages_redirect'),
]

# Serve static files in both development and production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)