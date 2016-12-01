from django.shortcuts import render

from rest_api.models import User


# Create your views here.
def index(request):
    if request.POST:
        pass
    else:
        return render(request, 'index.html')
