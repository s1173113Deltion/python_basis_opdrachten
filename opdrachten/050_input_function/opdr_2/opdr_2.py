# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Begin met een lijst van gasten
gastenlijst = ["Willem", "Paul", "Kees", "Marie", "Hilda"]

# Print de oorspronkelijke gastenlijst
print("Oorspronkelijke lijst:", gastenlijst)

# Marie belt dat ze niet meer meegaat, dus haal haar uit de lijst
gastenlijst.remove("Marie")

# Print de bijgewerkte gastenlijst
print("Na het verwijderen van Marie:", gastenlijst)

# George wil naast Kees zitten, voeg hem toe naast Kees
index_kees = gastenlijst.index("Kees")
gastenlijst.insert(index_kees + 1, "George")

# Print de definitieve gastenlijst
print("Definitieve lijst na toevoeging van George:", gastenlijst)
