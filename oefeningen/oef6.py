''' Maak een lijst met volgende steden: Kortrijk, Gent, Antwerpen, Mechelen,
Kluisbergen, Brussel, Brugge, Sint-Niklaas, Bornem, Luik, Charleroi'''

'''Kies er random 3 uit via een random selectie op de index. Indien de index even is,
vervang je de naam door streepjes. Indien de index oneven is door sterretjes.
Print de lijst af, waarbij de vervangingen zijn doorgevoerd'''

import random
steden = ['Kortrijk', 'Gent', 'Antwerpen', 'Mechelen', 'Kluisbergen', 'Brussel'\
          ,'Brugge', 'Sint-Niklaas', 'Bornem', 'Luik', 'Charleroi']


def streepjes(string):
    new_string = ""
    for i in string:
        new_string += '-'
    return new_string

def sterretjes(string):
    new_string = ''
    for i in string:
        new_string += '*'
    return new_string

indexes = random.sample(range(11), k=3)
for i in indexes:
    if i % 2 == 0:
        steden[i] = streepjes(steden[i])
    else:
        steden[i] = sterretjes(steden[i])

print(steden)