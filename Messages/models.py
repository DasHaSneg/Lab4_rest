from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Messages (models.Model):
    playerFrom = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_from')
    playerTo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_to')
    messageText = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.messageText

    class Meta:
        ordering = ('timestamp',)