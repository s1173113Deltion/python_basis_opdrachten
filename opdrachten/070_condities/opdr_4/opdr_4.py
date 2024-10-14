# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

# Hier de rest van jouw code...

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...

gevonden = False
for topping, prijs in toppings:
    if keuze == topping:
        print(f"U heeft {keuze} besteld. Dat kost {prijs}")
        gevonden = True

if not gevonden:
    print("Uw keuze zit niet in ons assortiment")
    
# Controleren of de keuze in de lijst van beschikbare toppings zit
topping_gevonden = False
for topping in toppings:
    if keuze == topping[0]:
        topping_gevonden = True
        print(f"U heeft {topping[0]} besteld. Dat kost {topping[1]}")
        break

if not topping_gevonden:
    print("Uw keuze zit niet in ons assortiment.")