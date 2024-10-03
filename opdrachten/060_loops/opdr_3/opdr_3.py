# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = []

# Loop van 3 tot 81, met stappen van 3
for i in range(3, 82, 3):  # 82 omdat range de bovenste limiet niet meerekent
    resultaat = (i ** 2) / 3  # Neem het kwadraat van i en deel door 3
    my_list.append(resultaat)  # Voeg het resultaat toe aan de lijst

# Print de lijst met resultaten
print(my_list)