# users/urls.py
from rest_framework import routers
from django.urls import path, include
from .views import SignUpView
from Lab4_rest import views
router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'inventory_type', views.InventoryTypeViewSet)
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('rest/', include(router.urls), name='rest'),
    path('api-Messages/', include('rest_framework.urls', namespace='rest_framework'))
]