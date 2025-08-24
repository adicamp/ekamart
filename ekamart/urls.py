"""
URL configuration for ekamart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from ekamart.views import menu_api_view

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('api/menu/', menu_api_view, name='api.menu'),
    path('master-user/', include('master_user.urls')),
    path('master-rak/', include('master_rak.urls')),
    path('master-shelving/', include('master_shelving.urls')),
    path('jwk-toko/', include('jwk_toko.urls')),
    path('supplier-reguler/', include('supplier_reguler.urls')),
    path('supplier-bkl/', include('supplier_bkl.urls')),
    path('max-inventory-dc/', include('max_inventory_dc.urls')),
    path('max-inventory-toko/', include('max_inventory_toko.urls')),
    path('store-registration/', include('store_registration.urls')),
    path('product-per-supplier/', include('product_per_supplier.urls')),
]
