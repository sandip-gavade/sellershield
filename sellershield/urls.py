"""
URL configuration for sellershield project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from accounts.views import login_view, logout_view, dashboard_view, order_view, return_view, dispute_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('logout/', logout_view, name='logout'),
    path('orders/', include('orders.urls')),
    path('returns/', include('returns.urls')),
    path('disputes/', include('disputes.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
