# Vraag de gebruiker om een getal tussen 1 en 60 in te geven. Druk alle cijfers af die je kan delen door 9.
user_number = int(input('Geef een getal tussen 1 en 60.'))
for i in range(user_number):
    if i % 9 == 0:
        print(i)
