from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from GameMap.models import Location
from django.core.cache import cache
Choices_class = (
 ('Knight', u'Knight'),
 ('Wizard', u'Wizard'),
 ('Thief', u'Thief'),
 ('Paladin', u'Paladin')
)
class Player(AbstractUser):
    # class Meta:
    #   app_label = 'Player'

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass
    hero_name = models.CharField(verbose_name=u'Hero Name', max_length=30)
    playerclass = models.CharField(verbose_name=u'Class', max_length=15, choices=Choices_class, default='Knight')
    email = models.CharField(verbose_name=u'Email', max_length=50)
    rank_level = models.IntegerField(verbose_name=u'Player level', default=0)
    position = models.ForeignKey(Location, default=1, on_delete=models.PROTECT)

    REQUIRED_FIELDS = ['email', 'hero_name', 'playerclass']
    def __str__(self):
       return self.username
    #
    # def last_seen(self):
    #     return cache.get('last_seen_%s' % self.user.username)
    #
    # def __unicode__(self):
    #     return self.name
    #
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Player.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.player.save()
