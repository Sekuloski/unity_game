import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from player.models import Player
from .serializers import PlayerSerializer


@api_view(['GET'])
def getPlayer(request, name):
    player = Player.objects.get(name=name)
    serializer = PlayerSerializer(player)

    return Response(serializer.data)


@api_view(['POST'])
def addPlayer(request):
    """
    {
        "name": "Bojan 6",
        "password": "password",
        "highscore": 0
    }
    """
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def setHighScore(request, name):
    player = Player.objects.get(name=name)
    """
    {
        "highscore": 100
    }
    """
    player.high_score = int(json.loads(request.body)['highscore'])
    player.save()

    return Response(PlayerSerializer(player).data)
