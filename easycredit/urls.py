"""
URL configuration for easycredit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework import routers
from products.views import ProductViewSet, ProductTypeViewSet, ProviderViewSet
from clients.views import ClientViewSet
from credits.views import CreditViewSet, PaymentViewSet
# from rest_framework.authtoken import views


router = routers.DefaultRouter()
# app products
router.register(r'products', ProductViewSet)
router.register(r'productTypes', ProductTypeViewSet)
router.register(r'providers', ProviderViewSet)

# app clients
router.register(r'clients', ClientViewSet)

# app credits
router.register(r'credits', CreditViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),  # Incluye todas las URLs de la API
    # path('api/token/', views.obtain_auth_token),
]
