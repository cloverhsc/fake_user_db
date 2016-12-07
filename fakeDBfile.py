# -*- coding: utf-8 -*-

# faker to produce fake data
from faker import Factory

# database model
from rest_api.models import User, HeartBeat, Breath, BloodPressure, BodyTemperature
from rest_api.models import Behavior, Wristband, Mattress, IndoorBehavior
from rest_api.models import BloodOxygen, Glycemia, UricAcid

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
    attend_doctor = fake.name()

    # customer information
    u = User.objects.create(
        name=fake.name(), age=age, sex=sex,
        weight=weight, height=height, contact=contact,
        address=address, attend_doctor=attend_doctor,
        bed_number=(x + 1), room_title='心臟科', room_number='1024'
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
    indoor = IndoorBehavior.objects.create(
        user=u, countleave=countleave, countcall=countcall)

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

        # blood oxygen 90 ~ 95
        bloodoxygen = BloodOxygen.objects.create(
            value=random.randint(90, 95), user=u
        )

        # uric acid 6.0 ~ 6.9
        uric_acid = UricAcid.objects.create(
            value=(6.0 + random.randrange(0, 9)/10.0), user=u
        )

        # glycemia 90 - 130
        glycemia = Glycemia.objects.create(
            value=random.randint(90, 130), user=u
        )

    u.save()
