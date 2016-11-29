# -*- coding: utf-8 -*-

# faker to produce fake data
from faker import Factory

# database model
from rest_api.models import User, HeartBeat, Breath, BloodPressure, BodyTemperature
from rest_api.models import Behavior, Wristband, Mattress, IndoorBehavior

# Django exceptions
from django.core.exceptions import ObjectDoesNotExist

import random

fake = Factory.create()

for x in range(6):
    age = random.randint(20, 80)
    if random.randint(1, 2) == 1:
        sex = 'M'
    else:
        sex = 'F'
    weight = random.randint(50, 150)
    height = random.randint(150, 220)
    contact = fake.phone_number()
    address = fake.address()

    # customer information
    u = User.objects.create(
        name=fake.name(), age=age, sex=sex,
        weight=weight, height=height, contact=contact,
        address=address
    )

    # customer walk steps information
    steps = random.randint(0, 10000)
    behavior = Behavior.objects.create(user=u, steps=steps)

    # customer wristband device power info
    if random.randint(1, 2) == 1:
        power = True
    else:
        power = False
    wristband = Wristband.objects.create(user=u, power=power)

    # customer mattress device power info
    if random.randint(1, 2) == 1:
        power = True
    else:
        power = False
    mattress = Mattress.objects.create(user=u, power=power)

    # customer indoor behavior info
    countleave = random.randint(0, 30)
    countcall = random.randint(0, 10)
    number = 1
    room = "天龍房"
    indoor = IndoorBehavior.objects.create(
        user=u, countleave=countleave,
        countcall=countcall,number=number,
        room=room
    )

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
