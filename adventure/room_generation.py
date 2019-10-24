from django.contrib.auth.models import User
from .models import Player, Room
import os
import random
import uuid

os.system( 'clear' )

class Maze:
    
    # def __init__( self ):
    #     self.size = None
    #     self.rooms = []
    
    def generate( size ):
        # size += 1
        the_map = []
        direction = []
        room_number = 1

        Room.objects.all().delete()
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
        end = 0
        for i in the_map:

            if end == size:
                roomList.append( [ i , 'The End' ] )
                # roomList.pop(len( roomList ) - 1)
                end += 1

            else:

                num1 = random.randint( 0 , len( adj ) - 1 )
                num2 = random.randint( 0 , len( noun ) - 1 )
                random_name1 = f'{adj[num1]} {noun[num2]}'

                roomList.append( [ i , random_name1 ] )
                end += 1

        os.system( 'clear' )

        print( '--------ROOMLIST-------\n' )
        for i in roomList:
            print( i )

        # # Add next room data
        for i in range( len( roomList ) - 1 ):

            roomList[i].append( roomList[i + 1][0][:1] )

        bloop = []

        print( '\n--------------------\n' )

        for i in range( len( roomList ) - 1 ):

            # print( '\n' )

            if i == 0:

                # print( 'Current Room:' , roomList[i][1] , roomList[i][0][1:] )
                # print( 'Next Room' , roomList[i + 1][1:] , roomList[i + 1][0][1:]  )

                room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                next_room = Room( id = roomList[i + 1][0][1] , title = f'{roomList[i + 1][1]}' , description = f'{roomList[i + 1][2]}' )
                bloop.append( [ room , next_room , "None" , i ] )

            if i >= 1:

                # print( 'Current Room:' , roomList[i][1:] , roomList[i][0][1:] )
                # print( 'Next Room' , roomList[i + 1][1:] , roomList[i + 1][0][1:]  )
                # print( 'Prev Room' , roomList[i - 1][1:] , roomList[i - 1][0][1:] )

                #roomid
                room = roomList[i][0][1]
                next_room = roomList[i + 1][0][1]
                prev_room = roomList[i - 1][0][1]

                room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'{roomList[i][2]}' )
                next_room = Room( id = roomList[i + 1][0][1] , title = roomList[i + 1][1] , description = roomList[i + 1][0] )
                prev_room = Room( id = roomList[i - 1][0][1] , title = roomList[i - 1][1] , description = roomList[i - 1][0][:1] )
                bloop.append( [ room , next_room , prev_room , i ] )

                if roomList[i + 1][1] == 'The End':

                    # print( 'Current Room:' , roomList[i][1:] , roomList[i][0][1:] )
                    # print( 'Prev Room' , roomList[i - 1][1:] , roomList[i - 1][0][1:] )

                    i += 1

                    room = Room( id = roomList[i][0][1] , title = f'{roomList[i][1]}' , description = f'THIS IS THE END' )
                    prev_room = Room( id = roomList[i - 1][0][1] , title = roomList[i - 1][1] , description = roomList[i - 1][0][:1] )
                    bloop.append( [ room , 'None' , prev_room , i ] )

        for i in bloop:

            i[0].save()

        count = 0


        for i in bloop:

            if count == 0:

                i[0].connectRooms( i[1] , i[0].description )

                players = Player.objects.all()
                for p in players:
                    p.currentRoom = i[1].id
                    p.save()

                count += 1

            else:

                count += 1

                # thank you next

                if i[1] == 'None':

                    i[0].connectRooms( i[2] , i[2].description )

                    
                    if i[0].description == 'n':
                        i[0].connectRooms( i[2] , 's' )

                    if i[0].description == 's':
                        i[0].connectRooms( i[2] , 'n' )

                    if i[0].description == 'e':
                        i[0].connectRooms( i[2] , 'w' )

                    if i[0].description == 'w':
                        i[0].connectRooms( i[2] , 'e' )

                else:

                    number = random.randint( 0 , 10 ) % 3

                    if number == 0:

                        num1 = random.randint( 0 , len( adj ) - 1 )
                        num2 = random.randint( 0 , len( noun ) - 1 )
                        random_name = f'{adj[num1]} {noun[num2]}'

                        branch = Room( id = i[0].id * 12 , title = random_name , description = 'Just a branch' )
                        branch.save()

                        if i[0].description == 'n':
                            i[0].connectRooms( branch , 's' )
                            branch.connectRooms( i[0] , 'n' )
                            i[0].description = i[0].description + ' & s'
                            print( 'Branch S of Room:' , i[0].id , i[0].description )
                            # branch = Room( id = i[0].id * 12 , title = random_name , description = 's' )

                        elif i[0].description == 's':
                            i[0].connectRooms( branch , 'n' )
                            branch.connectRooms( i[0] , 's' )
                            i[0].description = i[0].description + ' & n'
                            print( 'Branch North of Room:' , i[0].id , i[0].description )
                            # branch = Room( id = i[0].id * 12 , title = random_name , description = 'n' )

                        elif i[0].description == 'e':
                            i[0].connectRooms( branch , 'w' )
                            branch.connectRooms( i[0] , 'e' )
                            i[0].description = i[0].description + ' & w'
                            print( 'Branch West of Room:' , i[0].id , i[0].description)
                            # branch = Room( id = i[0].id * 12 , title = random_name , description = 'w' )

                        elif i[0].description == 'w':
                            i[0].connectRooms( branch , 'e' )
                            branch.connectRooms( i[0] , 'w' )
                            i[0].description = i[0].description + ' & e'
                            print( 'Branch East of Room:' , i[0].id , i[0].description )
                            # branch = Room( id = i[0].id * 12 , title = random_name , description = 'e' )

                        # branch.connectRooms( i[1] , i[1].description[:1] )
                        # branch.connectRooms( i[0] , i[1].description[:1] )

                        if branch.description == 'n':
                            branch.connectRooms( i[0] , 's' )

                        elif branch.description == 's':
                            branch.connectRooms( i[0] , 'n' )

                        elif branch.description == 'e':
                            branch.connectRooms( i[0] , 'w' )

                        elif branch.description == 'w':
                            branch.connectRooms( i[0] , 'e' )
                            

                    # # next_room
                    i[0].connectRooms( i[1] , i[0].description[:1] )

                    # r_foyer.connectRooms(r_overlook, "n")
                    # r_overlook.connectRooms(r_foyer, "s")
                    # r_foyer.connectRooms(r_narrow, "e")
                    # r_narrow.connectRooms(r_foyer, "w")

                    # current to previous
                    if i[0].description[:1] == 'n':
                        i[1].connectRooms( i[0] , 's' )

                    elif i[0].description[:1] == 's':
                        i[1].connectRooms( i[0] , 'n' )

                    elif i[0].description[:1] == 'e':
                        i[1].connectRooms( i[0] , 'w' )

                    elif i[0].description[:1] == 'w':
                        i[1].connectRooms( i[0] , 'e' )

                    # prev
                    if i[2].description[:1] == 'n':
                        i[0].connectRooms( i[2] , 's' )

                    elif i[2].description[:1] == 's':
                        i[0].connectRooms( i[2] , 'n' )

                    elif i[2].description[:1] == 'e':
                        i[0].connectRooms( i[2] , 'w' )

                    elif i[2].description[:1] == 'w':
                        i[0].connectRooms( i[2] , 'e' )

                    count += 1