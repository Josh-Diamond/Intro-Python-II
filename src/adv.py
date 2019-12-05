from room import Room
from player import Player
from item import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items
guitar = Item('Guitar', 'An Acoustic Guitar')
cd = Item('CD', 'A Shiny CD')
room['outside'].add_item(cd)
room['treasure'].add_item(guitar)
#
# Main
#
def play(name):
    global player
    if player.current_room == None:
        print("You can't go that way! GAME OVER")
        quit()
    else:
        print("You are currently at the", player.current_room)
        #print(player.current_room.description)
        explore = input("Explore the room? y, n?")
        if explore == "y":
            if len(player.current_room.items) > 0:
                print("You found this item:")
                print(f"{player.current_room.items[0].name}")
                pickup_item = input(
                    "Grab the item? y, n?")
                if pickup_item == 'y':
                    player.add_item(player.current_room.items[0])
            else:
                print(f"No items were found")

        location = input("Where would you like to go?")
        if location == "n":
            player.current_room = player.current_room.n_to

        elif location == "s":
            player.current_room = player.current_room.s_to

        elif location == "e":
            player.current_room = player.current_room.e_to

        elif location == "w":
            player.current_room = player.current_room.w_to

        elif location == "q":
            quit()

# Make a new player object that is currently in the 'outside' room.

# Game Start
name = input("What is your name?")
player = Player(name)
player.current_room = room['outside']
playing = True
print("Welcome to the Python Treasure game,", player.name)

while playing:
    play(name)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
