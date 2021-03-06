from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random

# DB
from rest_api.models import User, IndoorBehavior

# handle error
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@api_view(['POST'])
def get_list(request):
    id = []
    for user in User.objects.all():
        id.append(user.id)
    return Response({'list': id}, status=status.HTTP_200_OK)


@api_view(['POST'])
def profile(request):
    '''
     Find out customer's information
    '''
    result = {
        'result': 'error',
        'message': 'error',
    }
    id = request.data['id']
    try:
        user = User.objects.get(id=id)
    except ObjectDoesNotExist:
        result['message'] = 'Can not find user.'
    else:
        result['id'] = user.id
        result['name'] = user.name
        result['age'] = user.age
        result['sex'] = user.sex
        result['weight'] = user.weight
        result['contact'] = user.contact
        result['height'] = user.height
        result['address'] = user.address
        result['room_number'] = user.room_number
        result['room_title'] = user.room_title
        result['bed_number'] = user.bed_number
        result['attend_doctor'] = user.attend_doctor

        result['result'] = 'success'
        result['message'] = 'Success'
    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
def physiological(request):
    '''
     Find out customer's  physiological info randomly
    '''
    result = {
        'result': 'error',
        'message': 'error',
    }
    id = request.data['id']
    try:
        user = User.objects.get(id=id)
    except ObjectDoesNotExist:
        result['message'] = 'Can not find user.'
    else:
        # ervery user's physiological info is an range 0 - 19 array

        ht = user.heartbeat_set.all()
        result['heartbeat'] = random.choice(ht).heartbeat

        # breath
        breath = user.breath_set.all()
        result['breath'] = random.choice(breath).breath

        # blood pressure
        bloodpressure = user.bloodpressure_set.all()
        result['blood_pressure'] = random.choice(bloodpressure).bloodpressure

        # body temperature
        bodytemperature = user.bodytemperature_set.all()
        result['body_temperature'] = random.choice(bodytemperature).bodytemperature

        # indoor behavior information
        result['leave'] = user.indoorbehavior.leave
        result['count_leave'] = user.indoorbehavior.countleave
        result['call'] = user.indoorbehavior.call
        result['count_call'] = user.indoorbehavior.countcall

        # wristband
        result['wristband_power'] = user.wristband.power

        # mattress
        result['mattress_power'] = user.mattress.power

        # walk steps
        result['walk_steps'] = user.behavior.steps

        # blood oxygen
        bloodoxygen = user.bloodoxygen_set.all()
        result['blood_oxygen'] = random.choice(bloodoxygen).value

        # glycemia
        glycemia = user.glycemia_set.all()
        result['glycemia'] = random.choice(glycemia).value

        # uric acid
        uric_acid = user.uricacid_set.all()
        result['uric_acid'] = random.choice(uric_acid).value

        result['result'] = 'success'
        result['message'] = 'Success'
    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
def oncall_list(request):
    '''
     Find out on call paitent list and short information
     in this floor in this build.
    '''
    result = {
        'result': 'error',
        'message': 'error',
    }
    list = IndoorBehavior.objects.filter(call=True)

    if(len(list) == 0):
        result['detail_info'] = []
    else:
        result['detail_info'] = []
        for i in range(0, len(list)):
            name = list[i].user.name
            id = list[i].user.id
            room_title = list[i].user.room_title
            room_number = list[i].user.room_number
            bed_number = list[i].user.bed_number
            result['detail_info'].append(
                {
                    'id': id, 'name': name,
                    'room_title': room_title,
                    'room_number': room_number,
                    'bed_number': bed_number
                }
            )

    result['result'] = 'success'
    result['message'] = 'Success'
    return Response(result, status=status.HTTP_200_OK)
