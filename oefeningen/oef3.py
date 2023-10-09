# Vraag de gebruiker om een tekst in te geven. Tel het aantal letters en cijfers en druk deze dan af.
user_input = input('Insert text here!')
gebruikte_letters = []
gebruikte_cijfers = []

for teken in user_input:
    if teken.isalpha():
        gebruikte_letters.append(teken)
    elif teken.isdigit():
        gebruikte_cijfers.append(teken)

print(gebruikte_letters)
print(gebruikte_cijfers)