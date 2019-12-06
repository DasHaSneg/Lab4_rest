from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from GameMap.models import Location

Choices_class = (
 ('Knight', u'Knight'),
 ('Wizard', u'Wizard'),
 ('Thief', u'Thief'),
 ('Paladin', u'Paladin')
)
class Player(models.Model):
    class Meta:
        app_label = 'Player'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u'User Name', max_length=30, blank=True)
    playerclass = models.CharField(verbose_name=u'Class', max_length=15, choices=Choices_class, default='Knight')
    email = models.CharField(verbose_name=u'Email', max_length=50, blank=True)
    level = models.IntegerField(verbose_name=u'Player level', default=0)
    position = models.ForeignKey(Location, default=1, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Player.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.player.save()
