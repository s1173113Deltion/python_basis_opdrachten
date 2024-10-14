# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vragen = [
    "Wat vind je van de huidige regering?", 
    "Wat vind je van de Python-lessen tot nu toe?", 
    "Wat vind jij de mooiste stad van Nederland?"
]

with open("enquete_resultaten.txt", "at") as bestand:
    for vraag in vragen:
        antwoord = input(f"{vraag}\n")
        bestand.write(f"{vraag}\nAntwoord: {antwoord}\n\n")

print("De antwoorden zijn toegevoegd aan enquete_resultaten.txt")