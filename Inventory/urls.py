from django.urls import path, include

from Inventory import views, admin

urlpatterns = [
    path('Inventory/', views.ItemType_list, name="itemtype_list"),
    path('Inventory/(?P<pk>[0-9]+)/$', views.ItemType_detail, name="itemtype_details")
]
