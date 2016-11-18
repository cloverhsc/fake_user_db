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
     Find out user from id and get physiological info randomly
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
        result['name'] = user.name

        ht = user.heartbeat_set.all()
        result['heartbeat'] = random.choice(ht).heartbeat

        breath = user.breath_set.all()
        result['breath'] = random.choice(breath).breath

        bloodpressure = user.bloodpressure_set.all()
        result['bloodpressure'] = random.choice(bloodpressure).bloodpressure

        bodytemperature = user.bodytemperature_set.all()
        result['bodytemperature'] = random.choice(bodytemperature).bodytemperature

        result['result'] = 'success'
        result['message'] = 'Success'
    return Response(result, status=status.HTTP_200_OK)
