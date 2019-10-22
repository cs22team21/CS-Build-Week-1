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
    
    def generate( size ):
        size += 1
        the_map = []
        direction = []
        room_number = 1

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

        # LINKING THE ROOMS

        adj = [
            'Cyborg',
            'Rusty',
            'Beam',
            'Bionic',
            'Lazer',
            'Neon',
            'Chrome',
            'Clone',
            'Flooded',
            'Star Dust',
            'Moon Beam',
            'Ratio',
            'Alien',
            'Anti-Gravity',
            'Droid'
        ]

        noun = [
            'Lab',
            'Control Room',
            'Deck',
            'Cloning Facility',
            'Factory',
            'Holodeck',
            'Observatory',
            'Star Gate',
            'Hangar',
            'Chamber'
        ]

        roomList = []

        # add room names to the list
        for i in range( len( the_map ) - 1 ):

            end = size - 2
            if i == end:
                roomList.append( [ the_map[i] , 'The End' ] )
                # roomList.pop(len( roomList ) - 1)

            else:

                num1 = random.randint( 0 , len( adj ) - 1 )
                num2 = random.randint( 0 , len( noun ) - 1 )
                random_name1 = f'{adj[num1]} {noun[num2]}'

                roomList.append( [ the_map[i] , random_name1 ] )

        os.system( 'clear' )

        print( '--------ROOMLIST-------\n' )
        for i in roomList:
            print( i )

        # # Add next room data
        for i in range( len( roomList ) - 1 ):

            roomList[i].append( roomList[i + 1][0][:1] )


        Room.objects.all().delete()

        bloop = []

        print( '\n--------------------' )

        for i in range( len( roomList ) - 1 ):

            print( '\n\n' )

            if i == 0:

                print( 'Current Room:' , roomList[i][1] , roomList[i][0][1:] )
                print( 'Next Room' , roomList[i + 1][1:] , roomList[i + 1][0][1:]  )
                room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                next_room = Room( id = roomList[i + 1][0][1] , title = f'{roomList[i + 1][1]}' , description = f'{roomList[i + 1][2]}' )
                bloop.append( [ room , next_room , "None" , i ] )
            
            if i == len( roomList ) - 1:

                print( 'Current Room:' , roomList[i][1] , roomList[i][0][1:] )
                print( 'Prev Room' , roomList[i - 1][1:] , roomList[i - 1][0][1:]  )

                room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                prev_room = Room( id = roomList[i - 1][0][1] , title = f'{roomList[i - 1][1]}' , description = f'{roomList[i - 1][2]}' )
                bloop.append( [ room , "None" , prev_room , i ] )

            if roomList[i][1] == 'The End':

                print( 'Current Room:' , roomList[i][1:] , roomList[i][0][1:] )
                print( 'Prev Room' , roomList[i - 1][1:] , roomList[i - 1][0][1:] )

                room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                prev_room = Room( id = roomList[i - 1][0][1] , title = roomList[i - 1][1] , description = roomList[i - 1][0][:1] )
                bloop.append( [ room , 'None' , prev_room , i ] )

            elif i >= 1:

                print( 'Current Room:' , roomList[i][1:] , roomList[i][0][1:] )
                print( 'Next Room' , roomList[i + 1][1:] , roomList[i + 1][0][1:]  )
                print( 'Prev Room' , roomList[i - 1][1:] , roomList[i - 1][0][1:] )

                #roomid
                room = roomList[i][0][1]
                next_room = roomList[i + 1][0][1]
                prev_room = roomList[i - 1][0][1]

                room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                next_room = Room( id = roomList[i + 1][0][1] , title = roomList[i + 1][1] , description = roomList[i + 1][0] )
                prev_room = Room( id = roomList[i - 1][0][1] , title = roomList[i - 1][1] , description = roomList[i - 1][0][:1] )
                print( 'xxxxxxxxxxxx' , prev_room.description )
                bloop.append( [ room , next_room , prev_room , i ] )

        for i in bloop:

            i[0].save()

        count = 0

        print( '=======BLOOP=======\n' , bloop )

        for i in bloop:

            if count == 0:

                i[0].connectRooms( i[1] , i[0].description )

                count += 1

                players = Player.objects.all()
                for p in players:
                    p.currentRoom = i[0].id
                    p.save()

            else:

                # thank you next

                if i[1] == 'None':

                    os.system( 'clear' )

                    print( i )

                    i[0].connectRooms( i[2] , None )

                    count += 1

                else:

                    i[0].connectRooms( i[1] , i[0].description )

                    if i[2].description == 'n':
                        i[0].connectRooms( i[2] , 's' )

                    if i[2].description == 's':
                        i[0].connectRooms( i[2] , 'n' )

                    if i[2].description == 'e':
                        i[0].connectRooms( i[2] , 'w' )

                    if i[2].description == 'w':
                        i[0].connectRooms( i[2] , 'e' )

                    count += 1