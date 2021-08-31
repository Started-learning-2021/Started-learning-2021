#Adventure Game Objects
import random
from RockPaperScissors import rockpaperscissors 
from Rooms import rooms
from Coinflip import coinflip
from time import sleep  

Character_type = []

def Nowhere(): 
    exit() 

#Define Rooms and what happens 
def Ivanhoe(): 
    print("The kind people of Ivanhoe are wealthy and also hate the tyranical king.")
    sleep(2.5)
    print("You could ask someone for a magical stick to help you complete your quest: \n"\
    "1) Ask a citizen for their magical stick \n"\
    "2) Move to another location to aquire a magical stick. \n"\
    " \n")
    answer = input("Your choice > ")   
    if answer == "1":
        for i in range(1):
            result = random.randint(0,1)
            if result == 0:
                print("The citizen you ask hands you a magical stick requesting you use it to overthrow the tyranical king and lift the curse.")
                Magic_stick()
            elif result == 1:
                print("The citizen refuses to give you the stick. You will have to find one elsewhere")
        
    elif answer == "2":
        exit()

def Thornbury():
    input("You find a knife in the playground near a kid holding a magical stick. The decision seems obvious. \n"\
    "1) Pick up the knife, stab the child, take their stick? \n"\
    "2) Bargain with the child convince them to hand over the stick? \n"\
    " \n")
    answer = input("Your choice > ")  
   
    if answer == "1":
        print("You do the unthinkable in front of the child's parents and they attack you. \n"\
        "You weild the magical stick and realise it is just a regular stick. \n"\
        " \n")
        Game_over("The parents take the knife that you threw on the ground and stab you to death.")

    elif answer == "2":
        print("The child will not give you the stick and now the parents are getting involved. \n"\
        "You must find another way to acquire a magical stick. \n"\
        "Select another compass direction: ")
        #If answer 

def Brunswick():
    print("These hipsteps have the magical stick you need to complete your quest and seem below average intelligence. \n"\
        "You should approach one and challenge them to a game of rock, paper, scissors for their stick. \n"\
        "1) Press '1' to challenge hipster to rock, paper, scissors.")
    answer = input("> ")
        
    if answer == "1":
        rockpaperscissors()
    else:
        Game_over("Can't you follow basic instructions? \n"\
        "You die of starvation")  

def Heidelberg():
    print("There are lots of knife weilding hobos and youths around here. But noone has a magical stick. \n"\
    "You may fight a knife weilding hobo or youth for fun if you would like? \n"\
    "Your options are: \n"\
    "1) Fight a hobo \n"\
    "2) Fight a youth \n"\
    "3) Walk to another suburb \n"\
    " \n")
    answer = input("Your choice > ")  

    if answer == "1":
        print("You start a fight the hobo. He struggles to weild his knife and is malnourished. \n"\
        "You easily murder him and take his cloak. As an added bonus, it smells like wiskey. \n"\
        "You achieved very little and walk away quickly.")
        answer = input("Select a direction: ") 
        #If answer             

    elif answer == "2":
        print("You fight a youth.")
        Game_over("You fight a youth. \n"\
        "He was already weilding a knife and brutally stabs you to death.")

    elif answer == "3": 
        exit()

def Coburg():
    print("You can either: \n"\
    "1) Murder the imposter wizard for fun \n"\
    "2) Walk to another suburb \n"\
    " \n")           
    answer = input("Your choice > ") 

    if answer == "1":
        print("That was unnecassary. You seem to enjoy thinning out the herd. \n"\
        "You should walk to the next suburb quickly. Even if that guy deserved it.")
        exit()

    elif answer == "2":
        print("Wise decision. Walk to another suburb to complete your quest.")
        exit() #Is this the way to skip over the function?

def Macleod():
    print("You can either: \n"\
        "1) Get a coffee to stay alert \n"\
        "2) Walk to another suburb \n"\
        " \n")
    answer = input("Your choice > ") 
    if answer == "1":
        print("The coffee tastes good but the bartender was annoying. You may come back to murder people later.")
        exit()
    elif answer == "2":
        exit()

def Resivoir():
    print("There is a magical stick stuck in the mud in the middle of a swamp.")
    sleep(2.5)
    print("However, two idiots are already fighting to become the swamp king who wrestles it from the mud.")
    sleep(2.5)
    print("Select your method for aquiring the magical stick: \n"\
        "1) Challenge the other 2 men to games of rock, paper, scissors \n"\
        "2) Fight the other 2 men to the death as you are all evenly matched \n"\
        "3) Walk to another suburb \n"\
        " \n")
    answer = input("Your choice > ")

    if answer == "1":
        print("You manage to convince the two morons to play and knock each other out first.")
        sleep(2.5)
        print("Therefore you only need to win a single best of 3 game of rock, paper, scissors.")
        rockpaperscissors()
    elif answer == "2":
        for i in range(2):
            result = random.randint(0,2)
            if result == 0:
                Game_over("You have been murdered for a magical stick. Fortunately you always seem to reincarnate. ")
            elif result == 1:
                print("You manage to murder the other two idiots.")
                sleep(2)
                print("You walk over to the stick and wrestle it from the mud like King Arthur did with Excalibur. \n"\
                    "The magical stick is in your crusty hands.")
                Magic_stick()
            elif result == 2:
                exit()
            
def Fawkner():
    print("You can: \n"\
        "1) Take some meth with the local homeless population \n"\
        "2) Choose an alternative compass direction \n"\
        " \n") 
    answer = input("Your choice > ")

    if answer == "1":
        Game_over("You happily take meth with the homeless people but were not prepared for such a high dose. \n"\
        "You have died.")
    elif answer == "2": 
        exit()

def Teleport(): 
    if Magic_stick == True: 
        print("Would you like to teleport to the Tyranical King's base? \n"\
        " \n")
        answer = input("(Yes or No)").lower()

        if "y" or "yes" in answer: 
            Boss()

        elif "n" or "no" in answer: 
            Game_over("Your inaction causes you to starve to death.")

    if Magic_stick == False: 
        print("You are not a wizard and require more luck to teleport using the magical stick. \n"\
            "You must flip 3 heads in a row to boost your luck before teleporting.")
        coinflip()

def Boss():
    print("You find yourself in the Boss' room.")
    sleep(2)
    print("Dan Andrews, the Rockerfeller Family, the Pope and Jeffry Epstein are gathered around a table for a council meeting.")
    sleep(5)
    print("You knew something was wrong around here.")
    sleep(2)
    print("The pope is holding a Bedazzled Magical Stick like yours, but it's also sparkley.")
    sleep(3)
    print("His stick must be stopping you from teleporting outside the ring of steel... \n"\
        "You must kill the Pope first. \n"\
        " ")
    sleep(4)
    print("You have several options: \n"\
        "1) Bargain with this room of pitiful theives and pedos to undo the curse. \n"\
        "2) Murder the Pope and attempt to overthrow the council. \n"\
        "3) Teleport away but the stick only takes cowards to one location. \n"\
        " \n")
    answer = input("Your choice > ")
    if answer == "1":
        print("You should know better than to bargain with theives and pedophiles.")
        sleep(2.5)
        print("The magical stick does not work for cowards and disintegrates.")
        sleep(2.5) 
        Game_over("The Pope murders you immediately without remorse.")
        
    elif answer == "2":
        print("An epic battle ensues between you and the Pope.")
        sleep(2)
        print("fortunately his bedazzled magical stick cracks under pressure. He has been overusing it for mystical pleasure.")
        sleep(4.5)
        print("The Pope's servere overuse of the bedazzled magical stick undermines his magical prowess.")
        sleep(3)
        print("Although you can use magic to murder the Pope, you opt to behead him with your magical stick instead.")
        sleep(4)
        print("The remainder of the council are a bunch of cowards and in the face of death give you the keys to the kindgom. \n"\
            "You lift the curse and teleport safely outide the ring of steel. \n"\
            " \n")
        Win()

    elif answer == "3": 
        print("You should know better than to let theives and pedophiles rule the world.")
        sleep(2.5)
        Game_over("The magical stick does not work for cowards. It disintegrates and leaves you standed again.")
        
def Magic_stick(): #Need to fix
    if Character_type == "wizard": 
        Magic_stick == "True" 

    elif Character_type != "wizard":
        Magic_stick == "False"
        print("You aren't a wizard and require more luck to teleport using the magic stick.")
        sleep(2.5)
        print("You pull a coin from your pocket to attempt 3 heads in a row for the level of luck required.")
        print(" \n")
        sleep(3.5)
        answer = input("Flip the coin? (Yes / No)").lower() #NOT WORKING 
        if "y" or "yes": 
            coinflip()
        else:
            Game_over("You don't have what it takes to liberate the people and starve to death instead.")

def Start(): 
    current_room = rooms['Nowhere']
    print(' \n'\
    'You find yourself in {}.'.format(current_room['name']))
    sleep(4)
    if current_room['contents']:
        print('{}'.format(''.join(current_room['contents'])))   

def Play_again():
    answer = input("(Y or Yes)").lower()
    if "y" or "yes" in answer: 
        Start() 
    else: 
        print("You do not have what it takes to liberate the people. ")
        exit()

def Game_over(reason):
    print("\n" + reason)
    print("Game over!")
    Play_again()

def Win():
    print("Congratulations, you made the right decisions and managed to saved the people. \n"\
    "You are the people's champ!")
    sleep(5)
    Play_again()