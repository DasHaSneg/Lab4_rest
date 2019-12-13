from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from Lab4_rest import views

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'inventory_type', views.InventoryTypeViewSet)

urlpatterns = [

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('players/', include('Player.urls')),
    path('players/', include('django.contrib.auth.urls')),
    path('rest/', include(router.urls), name='rest'),
    path('api-Messages/', include('rest_framework.urls', namespace='rest_framework'))
]

