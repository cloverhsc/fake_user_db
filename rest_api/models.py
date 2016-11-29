# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


# handle error
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class User(models.Model):
    name = models.CharField(_('User name'), max_length=100)
    id = models.AutoField(primary_key=True)
    age = models.CharField(_('User age'), blank=True, max_length=3)
    sex = models.CharField(_('User sex'), max_length=1, blank=True)
    weight = models.CharField(_('User body weight'), blank=True, max_length=8)
    height = models.CharField(_('User height'), blank=True, max_length=8)
    contact = models.CharField(_('User contact number'), blank=True, max_length=16)
    address = models.CharField(_('User contact address'), blank=True, max_length=128)

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


class Behavior(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    steps = models.IntegerField(_('User walk steps'), default=0)

    class Meta:
        db_table = 'Behavior'


class Wristband(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    power = models.BooleanField(_('wristband no power or not'), default=False)

    class Meta:
        db_table = 'Wristband'


class Mattress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    power = models.BooleanField(_('mattress no power or not'), default=False)

    class Meta:
        db_table = 'Mattress'


class IndoorBehavior(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    leave = models.BooleanField(_('leave or here'), default=False)
    countleave = models.IntegerField(_('how many times leave room today'), default=0)
    call = models.BooleanField(_('Need help now'), default=False)
    countcall = models.IntegerField(_('how many times use call service'), default=0)
    number = models.CharField(_('room number'), max_length=32)
    room = models.CharField(_('room title'), max_length=128)

    class Meta:
        db_table = 'IndoorBehavior'
