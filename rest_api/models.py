from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


# handle error
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class User(models.Model):
    name = models.CharField(_('User name'), max_length=100)
    id = models.AutoField(primary_key=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['name']

    def __unicode__(self):
        return unicode(self.name)

    def get_name(self):
        '''
        Return user name.
        '''
        return unicode(self.name)

    class Meta:
        db_table = 'User'


class HeartBeat(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    heartbeat = models.IntegerField(_('heart beat counts'))

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['user', 'heartbeat']

    def get_user(self):
        return self.user

    class Meta:
        db_table = 'HeartBeat'


class Breath(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    breath = models.IntegerField(_('breath'))

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['user', 'breath']

    def get_user(self):
        return self.user

    class Meta:
        db_table = 'Breath'


class BloodPressure(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    bloodpressure = models.IntegerField(_('blood pressure'))

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['user', 'bloodpressure']

    def get_user(self):
        return self.user

    class Meta:
        db_table = 'BloodPressure'


class BodyTemperature(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    bodytemperature = models.CharField(_('body temperature'), max_length=128)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['user', 'bodytemperature']

    def get_user(self):
        return self.user

    class Meta:
        db_table = 'BodyTemperature'
