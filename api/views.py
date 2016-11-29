from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random

# DB
from rest_api.models import User

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
        result['name'] = user.name
        result['age'] = user.age
        result['sex'] = user.sex
        result['weight'] = user.weight
        result['contact'] = user.contact
        result['height'] = user.height
        result['address'] = user.address
        result['number'] = user.indoorbehavior.number
        result['room'] = user.indoorbehavior.room

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

        breath = user.breath_set.all()
        result['breath'] = random.choice(breath).breath

        bloodpressure = user.bloodpressure_set.all()
        result['bloodpressure'] = random.choice(bloodpressure).bloodpressure

        bodytemperature = user.bodytemperature_set.all()
        result['bodytemperature'] = random.choice(bodytemperature).bodytemperature

        result['leave'] = user.indoorbehavior.leave
        result['countleave'] = user.indoorbehavior.countleave
        result['call'] = user.indoorbehavior.call
        result['countcall'] = user.indoorbehavior.countcall

        result['result'] = 'success'
        result['message'] = 'Success'
    return Response(result, status=status.HTTP_200_OK)
