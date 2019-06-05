#!/usr/bin/python3
"""Author ACAGatela || Lab for List and Dict Modelling"""


def showInstructions():
    # print a main and the commands
    print('''
    RPG Game
    ========
    WIN the game by getting to the Garden with a key and a potion.
    Avoid the monster, but you can defeat the monster with a potion.
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    # print player's current status
    print('------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("------------------------")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {'Hall' : {'south' : 'Kitchen', 'east' : 'Dining Room', 'item' : 'key', 'north' : 'Living Room'}, 'Kitchen' : {'north' : 'Hall', 'item' : 'monster'}, 'Dining Room' : {'west' : 'Hall', 'item' : 'potion', 'south' : 'Garden'}, 'Garden' : {'north' : 'Dining Room'}, 'Living Room' : {'south' : 'Hall'}}

# start the player in the hall
currentRoom= 'Hall'

showInstructions()

#loop forever
while True:
    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #if there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    #if a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'potion' in inventory:
        print('You defeated the monster with the potion!')
        del rooms[currentRoom]['item']
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    #define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
