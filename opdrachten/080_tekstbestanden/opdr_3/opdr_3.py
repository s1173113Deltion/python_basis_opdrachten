# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:



def encrypt(text):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - ascii_offset + 5) % 26 + ascii_offset)
        else:
            encrypted_text += char

    return encrypted_text

# Gebruikersinvoer
text = input("Geef de tekst die wilt encrypten..\n")
print("\nGeëncrypteerde tekst:")
print(encrypt(text))
