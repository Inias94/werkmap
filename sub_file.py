def AND_gate(a, b):
    return a & b


""" 

Declareren via def():

def som(a, b, c):
    # a, b, c zijn de argumenten van de functie
    som_getallen = a + b + c
    #
    return som_getallen


def product(a, b, c)
    product = a * b * c
    return product


a = 1
b = 2
c = 3

z= 1
e= 5
a= 3

resultaat = som(a, b, c)
print(resultaat)

"""

def zoveelstekarakter(positie, tekst):
    maximum = len(tekst) -1
    if maximum < positie:
        return 'niet mogelijk' ### bij het gebruik van return wordt een functie gestopt.
    
    #char = positie in tekst
    char = tekst[positie]
    return char

lijst = ['appel', 'peer', 'banaan']
print(lijst[2][-2])


tekst = "Olivier"
positie = 3
print(len(tekst), tekst[5])





