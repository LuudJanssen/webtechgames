from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Game, HighScore
from .serializers import GameSerializer, HighScoreSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging
import json

logger = logging.getLogger(__name__)


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def index(request):
    return render(request, 'landing.html')


def game_view(request, game_id):
    game = Game.objects.get(game_id=game_id)
    game_highscores = HighScore.objects.filter(game_id=game_id).order_by('-score')[:10]
    context = {
        'game': game,
        'game_highscores': game_highscores
    }

    return render(request, 'game.html', context)


@api_view(['POST'])
def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    password_repeat = request.POST['password_repeat']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    if password != password_repeat:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name)
    authenticated = authenticate(username=username, password=password)

    if authenticated is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    login(request, authenticated)
    return Response(json.dumps({
        'username': username,
        'first_name': first_name,
        'last_name': last_name
    }), status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    authenticated = authenticate(username=username, password=password)

    if authenticated is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    login(request, authenticated)

    user = User.objects.get(username=username)

    return Response(json.dumps({
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name
    }), status=status.HTTP_200_OK)


@api_view(['GET'])
def logout_user(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def games(request):
    if request.method == 'GET':
        all_games = Game.objects.all()
        serializer = GameSerializer(all_games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def game(request, game_id):
    try:
        selected_game = Game.objects.get(game_id=game_id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GameSerializer(selected_game)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GameSerializer(selected_game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        selected_game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def highscores(request):
    if request.method == 'GET':
        all_highscores = HighScore.objects.all()
        serializer = HighScoreSerializer(all_highscores, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def highscore_game(request, game_id):
    try:
        selected_highscores = HighScore.objects.filter(game_id=game_id)
    except HighScore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HighScoreSerializer(selected_highscores, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def highscore_game_user(request, game_id, user_id):
    try:
        selected_highscores = HighScore.objects.filter(game_id=game_id).filter(user_id=user_id)
    except HighScore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HighScoreSerializer(selected_highscores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HighScoreSerializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(game_id=game_id, user_id=user_id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def highscore_id(request, id):
    try:
        selected_highscore = HighScore.objects.get(id=id)
    except HighScore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HighScoreSerializer(selected_highscore)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HighScoreSerializer(selected_highscore, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        selected_highscore.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
