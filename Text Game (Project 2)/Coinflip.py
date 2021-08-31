#Coinflip game
import random
from time import sleep
import math

def coinflip(): 
    heads = 0
    tails = 0
    flips = 0  

    for i in range(3):
        result = random.randint(0,1)
        flips += 1 
        sleep(1)
        if result == 0:
            heads += 1
            print("Heads")
        elif result == 1:
            tails += 1
            print("Tails")
    
    while True:
        if heads < 3:
            print("You did not get 3 heads in a row.")
            sleep(2)
            print("You try again because lives are at stake!")
            sleep(2)
            coinflip()
        if heads == 3:
            print("You have gathered enough luck to teleport to the King's liar for the final showdown!.")
            Magic_stick = True
            break