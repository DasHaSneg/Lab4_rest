from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from Player.models import Player


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Player
        fields = ('username', 'email', 'hero_name', 'playerclass')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Player
        fields = ('username', 'email', 'hero_name', 'playerclass')