from adventure.models import Room

roomList = []
visited = []

def makeRoom(x, y, room):
    w = 20
    h = 20

    if room not in visited:
            visited.append(room)
            if room.n_to != 0:
                north = {}
                north['x'] = x
                north['y'] = y - 40
                north['room'] = room.n_to
                line1 = x + 10
                line2 = y
                line3 = x + 10
                line4 = y - 20
                roomList.append([north['room'], north['x'], north['y'], line1, line2, line3, line4])
                makeRoom(north['x'], north['y'], Room.objects.get(id = north['room']))
            
            if room.s_to != 0:
                south = {}
                south['x'] = x
                south['y'] = y + 40
                south['room'] = room.s_to
                line1 = x + 10
                line2 = y + 20
                line3 = x + 10
                line4 = y + 40
                roomList.append([south['room'], south['x'], south['y'], line1, line2, line3, line4])
                makeRoom(south['x'], south['y'], Room.objects.get(id = south['room']))
            
            if room.e_to != 0:
                east = {}
                east['x'] = x + 2 * w
                east['y'] = y
                east['room'] = room.e_to
                line1 = x + 20
                line2 = y + 10
                line3 = x + 40
                line4 = y + 10
                roomList.append([east['room'], east['x'], east['y'], line1, line2, line3, line4])
                makeRoom(east['x'], east['y'], Room.objects.get(id = east['room']))

            if room.w_to != 0:
                west = {}
                west['x'] = x - 2 * w
                west['y'] = y
                west['room'] = room.w_to
                line1 = x
                line2 = y + 10
                line3 = x - 20
                line4 = y + 10
                roomList.append([west['room'], west['x'], west['y'], line1, line2, line3, line4])
                makeRoom(west['x'], west['y'], Room.objects.get(id = west['room']))

    return roomList