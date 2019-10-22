from django.contrib.auth.models import User
from .models import Player, Room
import os
import random
import uuid

os.system( 'clear' )

class Maze:
    
    def __init__( self ):
        self.size = None
        self.rooms = []

    def setup( room , next_room , prev_room , var ):

        # start room
        if prev_room == 'None':

            print( 'START ROOM' )
            var2 = str(int(var) + 1)
            var = room
            var2 = next_room
            var.save()
            var2.save()
            direction = room.description
            print( direction )
            # f'{int(var) + 1}' = next_room
            var.connectRooms( var2 , direction )
            players = Player.objects.all()
            for p in players:
                p.currentRoom = room.id
                p.save()

        # end room
        elif next_room == "None":

            print( 'END ROOM' )
            var2 = str(int(var) - 1)
            var = room
            var2 = prev_room
            var.save()
            direction = prev_room.description
            print( direction )

            if direction == 'n':
                reverse_direction = 's'
            elif direction == 's':
                reverse_direction = 'n'
            elif direction == 'w':
                reverse_direction = 'e'
            else:
                reverse_direction = 'w'

            var.connectRooms( var2 , reverse_direction )
            print( 'START GAME' )

        else:
            
            print( 'MID ROOM' )
            print( room.description )
            var2 = str(int(var) - 1)
            var3 = str(int(var) + 1)
            var = room
            var2 = prev_room
            var3 = next_room
            var.save()
            var2.save()
            var3.save()

            direction = prev_room.description
            print( direction )

            if direction == 'n':
                reverse_direction = 's'
            elif direction == 's':
                reverse_direction = 'n'
            elif direction == 'w':
                reverse_direction = 'e'
            else:
                reverse_direction = 'w'

            var.connectRooms( var2 , reverse_direction )
            var.connectRooms( var3 , room.description )



            # var = Room( title = room.title, description = room.description )

            # room_one = Room(title="Outside Cave Entrance", description="North of you, the cave mount beckons")
            # room_two = Room(title="Foyer", description="Dim light filters in from the south. Dusty passages run north and east.")
            # room_three = Room(title="three", description="North of you, the cave mount beckons")
            # room_four = Room(title="Four", description="Dim light filters orth and east.")

            # room_connections.append( var )
            # var.save()
            # print( 'Connections' , room_connections )

            # room_one.save()
            # room_two.save()
            # room_three.save()
            # room_four.save()

            # room_one.connectRooms(room_two, "n")

            # room_two.connectRooms(room_three, "w")
            # room_two.connectRooms(room_one, "s")

            # room_three.connectRooms( room_four, 'n' )
            # room_three.connectRooms( room_two, 'e' )

            # room_four.connectRooms( room_three, 's' )
    
    def generate( size ):
        size = size
        the_map = ['start']
        direction = []
        room_number = 0

        for i in range( size ):

            ran_num = random.randint( 4 , 100 ) % 4

            # GO NORTH
            if ran_num == 0:

                if direction == []:
                    direction.append( 'Moving_North' )
                    the_map.append( f'n{room_number}' )
                    room_number += 1

                # if going South and want to move North, that reverses what just happened
                if direction[ len( direction ) - 1 ] == 'Moving_South':

                    num = random.randint( 4 , 100 ) % 3

                    if num == 0:
                        the_map.append( f'w{room_number}' )
                        direction.append( 'Moving_West' )
                        room_number += 1

                    elif num == 1:
                        the_map.append( f's{room_number}' )
                        direction.append( 'Moving_South' )
                        room_number += 1

                    else:
                        the_map.append( f'e{room_number}' )
                        direction.append( 'Moving_East' )
                        room_number += 1


                else:
                    the_map.append( f'n{room_number}' )
                    direction.append( 'Moving_North' )
                    room_number += 1

            # GO SOUTH
            elif ran_num == 1:

                if direction == []:
                    direction.append( 'Moving_South' )
                    the_map.append( f's{room_number}' )
                    room_number += 1
                
                # if going North and want to move South, that reverses what just happened
                if direction[ len( direction ) - 1 ] == 'Moving_North':

                    num = random.randint( 4 , 100 ) % 3

                    if num == 0:
                        the_map.append( f'w{room_number}' )
                        direction.append( 'Moving_West' )
                        room_number += 1

                    elif num == 1:
                        the_map.append( f'n{room_number}' )
                        direction.append( 'Moving_North' )
                        room_number += 1

                    else:
                        the_map.append( f'e{room_number}' )
                        direction.append( 'Moving_East' )
                        room_number += 1
                        
                else:

                    the_map.append( f's{room_number}' )
                    direction.append( 'Moving_South' )
                    room_number += 1

            # GO EAST
            elif ran_num == 2:

                if direction == []:
                    direction.append( 'Moving_East' )
                    the_map.append( f'e{room_number}' )
                    room_number += 1

                # if going West and want to move East, that reverses what just happened
                if direction[ len( direction ) - 1 ] == 'Moving_West':

                    num = random.randint( 4 , 100 ) % 3

                    if num == 0:
                        the_map.append( f's{room_number}' )
                        direction.append( 'Moving_South' )
                        room_number += 1

                    elif num == 1:
                        the_map.append( f'w{room_number}' )
                        direction.append( 'Moving_West' )
                        room_number += 1

                    else:
                        the_map.append( f'n{room_number}' )
                        direction.append( 'Moving_North' )
                        room_number += 1

                else:
                    the_map.append( f'e{room_number}' )
                    direction.append( 'Moving_East' )
                    room_number += 1

            # GO WEST
            else:

                if direction == []:
                    direction.append( 'Moving_West' )
                    the_map.append( f'w{room_number}' )
                    room_number += 1

                # if going East and want to move West, that reverses what just happened
                if direction[ len( direction ) - 1 ] == 'Moving_East':

                    num = random.randint( 4 , 100 ) % 3

                    if num == 0:
                        the_map.append( f'n{room_number}' )
                        direction.append( 'Moving_North' )
                        room_number += 1

                    elif num == 1:
                        the_map.append( f'e{room_number}' )
                        direction.append( 'Moving_East' )
                        room_number += 1

                    else:
                        the_map.append( f's{room_number}' )
                        direction.append( 'Moving_South' )
                        room_number += 1

                else:
                    the_map.append( f'w{room_number}' )
                    direction.append( 'Moving_West' )
                    room_number += 1

        # the_map.append( 'End' )

        # LINKING THE ROOMS

        adj = [
            'Cyborg',
            'Rusty',
            'Beam',
            'Bionic',
            'Lazer',
            'Neon',
            'Chrome',
            'Clone'
        ]

        noun = [
            'Lab',
            'Control Room',
            'Deck',
            'Cloning Facility',
            'Factory',
            'Holodeck'
        ]

        roomList = []

        # add rooms next room to the roomList
        for i in range( len( the_map ) - 1 ):

            num1 = random.randint( 0 , len( adj ) - 1 )
            num2 = random.randint( 0 , len( noun ) - 1 )
            random_name1 = f'{adj[num1]} {noun[num2]}'

            roomList.append( [ the_map[i] , random_name1 ] )

        os.system( 'clear' )

        # # Add next room data
        for i in range( len( roomList ) - 1 ):

            roomList[i].append( roomList[i + 1][0][:1] )


        Room.objects.all().delete()

        for i in range( len( roomList ) - 1 ):

            if i == 0:
                room = Room( title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                next_room = Room( title = f'{roomList[i + 1][1]}' , description = f'{roomList[i + 1][2]}' )
                Maze.setup( room , next_room , "None" , f"{i}" )
            
            if i == len( roomList ) - 2:
                room = Room( title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                prev_room = Room( title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                Maze.setup( room , "None" , prev_room , f"{i}" )

            else:

                room = Room( title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                next_room = Room( title = f'{roomList[i + 1][1]}' , description = f'{roomList[i + 1][2]}' )
                prev_room = Room( title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                Maze.setup( room , next_room , prev_room , f"{i}" )




        # ok = []



        # for i in range( len( roomList ) - 1 ):

        #     roomId = count
        #     roomId = Room( title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
        #     print( '--------' , type( roomId ) )
        #     ok.append( roomId )
        #     count += 1

        # for i in range( len( ok ) ):

        #     print( ok[i].title , ok[i].description )
        #     ok[i].save()

        #     if i >= 1:
        #         prev_room = ok[i - 1]
        #     elif i < len( ok ) - 1:
        #         next_room = ok[i + 1]

        #     if i == 0:
        #         ok[i].connectRooms( next_room , ok[i].description )

        #     elif i == len( ok ) - 1:

        #         if prev_room.description == "n":
        #             ok[i].connectRooms( prev_room , "s" )
        #         elif prev_room.description == "s":
        #             ok[i].connectRooms( prev_room , "n")
        #         elif prev_room.description == "e":
        #             ok[i].connectRooms( prev_room , "w" )
        #         elif prev_room.description == "w":
        #             ok[i].connectRooms( prev_room , "e" )

        #     else:

        #         ok[i].connectRooms( next_room , next_room.description )

        #         if prev_room.description == "n":
        #             ok[i].connectRooms( prev_room , "s" )
        #         elif prev_room.description == "s":
        #             ok[i].connectRooms( prev_room , "n")
        #         elif prev_room.description == "e":
        #             ok[i].connectRooms( prev_room , "w" )
        #         elif prev_room.description == "w":
        #             ok[i].connectRooms( prev_room , "e")

        # start_room = Room( id = 0 , title = f'{roomList[0][1]}' , description = f'{roomList[i][2]}'  )

                

# m = Maze()
# 12 rooms
# m.generate( 10 )
# 52 rooms
# m.generate( 50 )