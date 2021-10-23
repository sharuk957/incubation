from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Incubation
from .serializers import registrationlistserializer
from django.db.models import Q
# Create your views here.

@api_view(['GET'])
def getrouter(request):
    return Response("hi")


@api_view(['GET'])
def new_application(request):
    data = Incubation.objects.filter(Status="New")
    serializer =registrationlistserializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pending_application(request):
    data = Incubation.objects.filter(~Q(Status="New"))
    serializer =registrationlistserializer(data,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def one_application(request,id):
    data = Incubation.objects.get(id=id)
    serializer =registrationlistserializer(data,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def recordtrack(request):
    data = Incubation.objects.all()
    serializer =registrationlistserializer(data,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registration(request):
    data=request.data
    print(data)
    return Response('added')