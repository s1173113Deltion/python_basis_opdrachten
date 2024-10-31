# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Lijst om alle feestgangers op te slaan
feestgangers = []

# Functie om input te vragen en op te slaan in een dictionary
def feestganger_invoeren():
    antwoorden = {}
    # Vragen aan de feestganger
    antwoorden['voornaam'] = input(f"1. {vragen[0]} \n> ")
    antwoorden['achternaam'] = input(f"2. {vragen[1]} \n> ")
    antwoorden['drank'] = input(f"3. {vragen[2]} \n> ")
    antwoorden['eten'] = input(f"4. {vragen[3]} \n> ")

    # Opslaan van de feestganger in de lijst
    feestgangers.append(antwoorden)
    
    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")

# Herhaal invoer voor meerdere feestgangers
while True:
    feestganger_invoeren()
    nog_een = input("Wil je nog een feestganger toevoegen? (ja/nee): ").lower()
    if nog_een != 'ja':
        break

# Opslaan van de gegevens in een tekstbestand
with open('feestgangers_gegevens.txt', 'a') as file:
    for feestganger in feestgangers:
        file.write("----\n")
        for key, value in feestganger.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")