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
        # Vider la bdd
        Station.objects.all().delete()
        Line.objects.all().delete()

        # 1. recup lines
        r = requests.get('https://api-ratp.pierre-grimaud.fr/v3/lines/metros?_format=json')
        linesJson = json.loads(r.text)['result']['metros']

        lineArray = []
        stationArray = []

        for lineJson in linesJson:
            line = Line()
            line.letter = lineJson['code']

            directions = lineJson['directions'].split(' / ')
            line.directionA = directions[0]

            if len(directions) >= 2:
                line.directionA = directions[1]

            line.save()
            lineArray.append(line)

        # 2. recup stations
        for line in lineArray:
            r = requests.get('https://api-ratp.pierre-grimaud.fr/v3/stations/metros/' + line.letter)
            stationsJson = json.loads(r.text)['result']['stations']

            for stationJson in stationsJson:
                if any(existingStation.name == stationJson['name'] for existingStation in stationArray):
                    station = [existingStation for existingStation in stationArray if existingStation.name == stationJson['name']][0]
                    station.lines.add(line)
                    station.save()
                else:
                    station = Station()
                    station.name = stationJson['name']
                    stationArray.append(station)
                    station.save()
                    station.lines.add(line)
                    station.save()

        print('over')
        return JsonResponse({}, status=200)
    return JsonResponse({}, status=400)