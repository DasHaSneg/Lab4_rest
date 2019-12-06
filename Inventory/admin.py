from django.contrib import admin
from Inventory.models import ItemType, Item


class Inventory_Admin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Item, Inventory_Admin)