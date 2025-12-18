# Author : Cesar Vivas


# each key char will represent the  nun of rotation of each char part of the cipher text
# vigenere program

# ENGLISH ALPHABET
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def vigenere_encrypt(phrase, key):
    encrypted = ""
    key_index = 0
    for char in phrase:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = (
                UPPER_ALPHABET.index(key_char.upper())
                if key_char.isalpha()
                else 0
            )

            if char in UPPER_ALPHABET:
                letter = UPPER_ALPHABET.index(char)
                encrypted += UPPER_ALPHABET[(letter + shift) % 26]
            else:
                letter = LOWER_ALPHABET.index(char)
                encrypted += LOWER_ALPHABET[(letter + shift) % 26]

            key_index += 1
        else:
            encrypted += char

    return encrypted


def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            shift = (
                UPPER_ALPHABET.index(key_char.upper())
                if key_char.isalpha()
                else 0
            )

            if char in UPPER_ALPHABET:
                letter = UPPER_ALPHABET.index(char)
                decrypted += UPPER_ALPHABET[(letter - shift) % 26]
            else:
                letter = LOWER_ALPHABET.index(char)
                decrypted += LOWER_ALPHABET[(letter - shift) % 26]

            key_index += 1
        else:
            decrypted += char

    return decrypted

#  run test code
encrypted = vigenere_encrypt(phrase, key)
print("Encrypted:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Decrypted:", decrypted)
