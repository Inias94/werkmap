# Maak een spel dat de gebruiker een getal tussen de 1 en 20 moet raden.
# Als de gebruiker een cijfer ingeeft dat dan krijgt hij een hint of het kleiner of groter is.
# Voeg ook een optie toe zodat de gebruiker kan stoppen indien hij het spel beu is.
import random

player_guess = ''
random_number = random.randint(1,20)

def gok():
    
    if player_guess == random_number:
        print('well done, you have won')
    elif player_guess < random_number:
        input('You guessed too low, try again pick 0 to quit')
    else:
        print('You guessed to high!, try again pick 0 to quit')

while player_guess != random_number:
    player_guess = int(input("Raad een getal tussen 1 en 20!"))
    if player_guess == 0:
         break
    gok()