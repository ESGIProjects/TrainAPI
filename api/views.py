import requests, json

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Schedule, Line, Driver, Train, Station
from .serializers import ScheduleSerializer, LineSerializer, DriverSerializer, TrainSerializer, StationSerializer, UserSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]


class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    permission_classes = [IsAuthenticated]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


@csrf_exempt
def ratp_api_call(request):
    if request.method == 'GET':

        # 1. Lignes de métro
        r = requests.get('https://api-ratp.pierre-grimaud.fr/v3/lines/metros?_format=json')
        metroLinesResponse = json.loads(r.text)
        metroIds = []

        for item in metroLinesResponse['result']['metros']:
            metro = Line()
            metro.letter = item['code']
            metroIds.append(item['code'])
            directions = item['directions'].split(' / ')
            metro.directionA = directions[0]
            if len(directions) >= 2:
                metro.directionB = directions[1]
            metro.save()

        # 2. Stations
        for lineCode in metroIds:
            r = requests.get('https://api-ratp.pierre-grimaud.fr/v3/stations/metros/'+lineCode)
            stationsLinResponse = json.loads(r.text)

            #for item in stationsLinResponse['result']['stations']:
            #    station = Station()
           #     station.lines

        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)

