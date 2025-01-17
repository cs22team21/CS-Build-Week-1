from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
from .room_generation import Maze
from .dungeon import makeRoom

# instantiate pusher
#pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))
@csrf_exempt
@api_view(["GET"])
def position(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'n_to': room.n_to, 'w_to': room.w_to, 's_to': room.s_to, 'e_to': room.e_to, 'id': room.id}, safe=True)
@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    Maze.generate(100)
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'n_to': room.n_to, 'w_to': room.w_to, 's_to': room.s_to, 'e_to': room.e_to, 'id': room.id}, safe=True)


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        #for p_uuid in currentPlayerUUIDs:
        #   pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        #for p_uuid in nextPlayerUUIDs:
        #    pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'n_to': nextRoom.n_to, 's_to': nextRoom.s_to, 'e_to': nextRoom.e_to, 'w_to': nextRoom.w_to, 'players':players, 'error_msg':"",'id': nextRoomID}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way.", "id": room.id}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    pass

@csrf_exempt
@api_view(["GET"])
def get_rooms(request):
    rooms = []
    for room in Room.objects.all():
        players = room.playerNames(request.user.player.id)
        data = {
            'title': room.title,
            'description': room.description,
            'id': room.id,
            'n_to': room.n_to,
            's_to': room.s_to,
            'e_to': room.e_to,
            'w_to': room.w_to,
            'players': players
        }
        rooms.append(data)
    return JsonResponse({"rooms": rooms})

@csrf_exempt
@api_view(["GET"])
def grid(request):
    return JsonResponse({"grid": makeRoom(400, 400, Room.objects.first())})
