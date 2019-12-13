from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Player.forms import CustomUserCreationForm, CustomUserChangeForm
from Player.models import Player


# class Player_Admin(admin.ModelAdmin):
#     list_display = ('name',)
#
#
# admin.site.register(Player, Player_Admin)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Player
    list_display = ['username', 'email', 'hero_name', 'playerclass', 'rank_level', 'position',]


admin.site.register(Player, CustomUserAdmin)