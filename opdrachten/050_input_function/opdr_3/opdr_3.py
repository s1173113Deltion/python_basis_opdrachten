# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om een lijst met minimaal 5 objecten in te vullen, gescheiden door komma's
invoer = input("Voer een lijst van objecten in, gescheiden door komma's (bijv. steden): ")

objecten = [item.strip() for item in invoer.split(",")]

# Sorteer de lijst in omgekeerde alfabetische volgorde
objecten.sort(reverse=True)

# Print de gesorteerde lijst
print(objecten)