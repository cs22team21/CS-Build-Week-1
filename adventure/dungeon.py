from adventure.models import Room

visited = []
roomList = []

def makeRoom(x, y, room):
    w = 20
    h = 20
    north = {}
    south = {}
    east = {}
    west = {}

    for room in Room.objects.all():
        print(room)
    
    if room.n_to == 0 and room.s_to == 0 and room.e_to == 0 and room.w_to == 0:
        pass
    else:
        if room.n_to != 0 and room.n_to not in visited:
            north['x'] = x
            north['y'] = y - 2 * h
            north['room'] = room.n_to
            line1 = north['x'] + 10
            line2 = north['y']
            line3 = north['x'] + 10
            line4 = north['y'] + 40
            roomList.append([north['room'], north['x'], north['y'], line1, line2, line3, line4])
            visited.append(north['room'])
            makeRoom(north['x'], north['y'], Room.objects.get(id = north['room']))

        if room.s_to != 0 and room.s_to not in visited:
            south['x'] = x
            south['y'] = y + 2 * h
            south['room'] = room.s_to
            line1 = south['x'] + 10
            line2 = south['y'] - 40
            line3 = south['x'] + 10
            line4 = south['y']
            roomList.append([south['room'], south['x'], south['y'], line1, line2, line3, line4])
            visited.append(south['room'])
            makeRoom(south['x'], south['y'], Room.objects.get(id = south['room']))
        
        if room.e_to != 0 and room.e_to not in visited:
            east['x'] = x + 2 * w
            east['y'] = y
            east['room'] = room.e_to
            line1 = east['x'] + 40
            line2 = east['y'] + 10
            line3 = east['x']
            line4 = east['y'] + 10
            roomList.append([east['room'], east['x'], east['y'], line1, line2, line3, line4])
            visited.append(east['room'])
            makeRoom(east['x'], east['y'], Room.objects.get(id = east['room']))
        
        if room.w_to != 0 and room.w_to not in visited:
            west['x'] = x - 2 * w
            west['y'] = y
            west['room'] = room.w_to
            line1 = west['x'] - 40
            line2 = west['y'] + 10
            line3 = west['x']
            line4 = west['y'] + 10
            roomList.append([west['room'], west['x'], west['y'], line1, line2, line3, line4])
            visited.append(west['room'])
            makeRoom(west['x'], west['y'], Room.objects.get(id = west['room']))
    return roomList