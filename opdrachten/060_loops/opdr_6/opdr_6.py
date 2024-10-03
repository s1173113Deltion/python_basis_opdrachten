# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizza_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizza_list.sort()
print("Gesorteerde pizza's:", pizza_list)

# Voeg een extra pizza toe
pizza_list.append('shoarma')
print("Na toevoeging van een pizza:", pizza_list)

# Verwijder de pizza die je het minst lekker vindt
pizza_list.remove('olivio')
print("Na verwijderen van een pizza:", pizza_list)

# Print de eerste 3 pizza's uit de lijst
print("Eerste 3 pizza's:", pizza_list[:3])

# Print alleen de middelste pizza uit de lijst
middle_index = len(pizza_list) // 2
print("Middelste pizza:", pizza_list[middle_index:middle_index + 1])

# Print de laatste 3 pizza's uit de lijst
print("Laatste 3 pizza's:", pizza_list[-3:])