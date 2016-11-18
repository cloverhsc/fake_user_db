# -*- coding: utf-8 -*-

# faker to produce fake data
from faker import Factory

# database model
from rest_api.models import User, HeartBeat, Breath, BloodPressure, BodyTemperature

# Django exceptions
from django.core.exceptions import ObjectDoesNotExist

import random

fake = Factory.create()

for x in range(12):
    u = User.objects.create(name=fake.name())
    for y in range(20):
        ht = HeartBeat.objects.create(
            heartbeat=random.randint(80, 160), user=u
        )
        breath = Breath.objects.create(
            breath=random.randint(15, 20), user=u
        )
        bloodpressure = BloodPressure.objects.create(
            bloodpressure=random.randint(100, 120), user=u
        )
        # 36.8±0.7℃
        bodytemperature = BodyTemperature.objects.create(
            bodytemperature=(36.8 + random.randrange(-7, 7)/10.0), user=u
        )

    u.save()
