"""
Object Adventure Game
"""
from Objects import Start
from Rooms import rooms 
from time import sleep

current_room = rooms['Nowhere']
directions = ['north', 'north east', 'north west', 'east', 'south', 'south east', 'south west', 'west']

Character_type = []
Character_type = input("Select your character type... \n"\
"Generally warrior or wizard works best but I won't stop you becoming a pickle: ").lower()
Hat_colour = []
Hat_colour = input("Select a hat colour: ").lower()
Hat = []
if Character_type == "wizard":
    Hat = "wizard's hat"
elif Character_type != "wizard": 
    Hat = "helmet"

print(' \n'\
"You are a {} wearing a {} {}.".format(Character_type, Hat_colour, Hat))
print("Let's start your journey... \n"\
    " ")
sleep(1.5)
print("You find yourself deserted in a strange and unfamiliar land.")
sleep(3)
print("You are keen to explore the vast world in your Burkinstocks.")
sleep(3.5)
print("However, you sense a magical force preventing travel beyond 5km in any direction.")
sleep(4)
print("There may be no choice but to find and mutilate the tyranical king who has foresaken the land.")
sleep(4)
print("The 5km ring of steel is invisible and incinerates anything attemping to cross. \n"\
    " ")
sleep(4)
print("Fuck the king.")

#Initiate start of game after storyline. 
Start()

# game loop
while True:
    # display current location
    print(' \n'\
    'You find yourself in {}.'.format(current_room['name']))
    sleep(4)
    if current_room['contents']:
        print('{}'.format(''.join(current_room['contents']))),
        print('{}'.format(''.join(current_room['function'+()]))) #This is probably wrong. 

    sleep(5)
    command = input('\nWhich direction do you choose? ').lower().strip()
    # movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            # bad movement
            print("You can't go that way.")
    # quit game
    elif command.lower() in ('q', 'quit'):
        break

#If the player decides not to use teleportation -> starve to death, game over. 