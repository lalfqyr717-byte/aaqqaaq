from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='index_redirect'),
    path('admin/', admin.site.urls),
    path('api/health/', views.health_check, name='health_check'),
    path('api/auth/login/', views.auth_login, name='auth_login'),
    path('api/session/', views.api_session, name='api_session'),
    path('api/sync/', views.api_sync, name='api_sync'),
]

# Serve pages HTML files
urlpatterns += [
    path('pages/sales.html', TemplateView.as_view(template_name='pages/sales.html'), name='sales_page'),
    path('pages/products.html', TemplateView.as_view(template_name='pages/products.html'), name='products_page'),
    path('pages/purchases.html', TemplateView.as_view(template_name='pages/purchases.html'), name='purchases_page'),
    path('pages/clients.html', TemplateView.as_view(template_name='pages/clients.html'), name='clients_page'),
    path('pages/suppliers.html', TemplateView.as_view(template_name='pages/suppliers.html'), name='suppliers_page'),
    path('pages/warehouse.html', TemplateView.as_view(template_name='pages/warehouse.html'), name='warehouse_page'),
    path('pages/employees.html', TemplateView.as_view(template_name='pages/employees.html'), name='employees_page'),
    path('pages/installments.html', TemplateView.as_view(template_name='pages/installments.html'), name='installments_page'),
    path('pages/reports.html', TemplateView.as_view(template_name='pages/reports.html'), name='reports_page'),
    path('pages/settings.html', TemplateView.as_view(template_name='pages/settings.html'), name='settings_page'),
]

# Serve static files in both development and production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)