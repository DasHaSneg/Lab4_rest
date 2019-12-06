from django.contrib import admin
from Player.models import Player


class Player_Admin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Player, Player_Admin)