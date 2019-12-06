from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Lab4_rest import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'inventory_type', views.InventoryTypeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-Messages/', include('rest_framework.urls', namespace='rest_framework'))
]

