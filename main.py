# Enigma Machine
# author: Cesar Vivas

import os
 #-------------------GLOBAL CONSTANTS----------------------------

# ENGLISH ALPHABET
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FILE_EXTENSION =".txt"


# CIPHER(VIGENERE)
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
# Decryption(VIGENERE)
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

# ------------------ WRITING OVER/ OPENING FILES ------------------
def create_encrypted_file():
    filename = input("Enter file name (without extension): ").strip() + FILE_EXTENSION
    message = input("Enter your message: ")
    key = input("Enter encryption key: ").strip()


    if not key.isalpha():
        print("Key must contain letters only.")
        return

    # output
    encrypted_message = vigenere_encrypt(message, key)

    # option not to to avoid  overwrite if file already exist
    if os.path.exists(filename):
        overwrite = input("File exists. Overwrite? (y/N): ").lower()
        if overwrite != "y" or "yes":
            return


    with open(filename, "w") as file:
        file.write(encrypted_message)


    print(f"Encrypted message saved to '{filename}'")




def decrypt_file():
    filename = input("Enter filename to decrypt (without extension): ").strip() + FILE_EXTENSION


    if not os.path.exists(filename):
        print("File not found.")
        return
    if os.path.exists(filename):
        overwrite = input("File exists. Overwrite? (y/N): ").lower()
        while overwrite == "y" or "yes":
            with open(filename, "w") as file:
                message = input("Enter your message: ")
                key = input("Enter encryption key: ").strip()

                if not key.isalpha():
                    print("Key must contain letters only.")
                    return
                # output
                encrypted_message = vigenere_encrypt(message, key)
                with open(filename, "w") as file:
                    file.write(encrypted_message)

                print(f"Encrypted message saved to '{filename}'")


    key = input("Enter decryption key: ").strip()


    if not key.isalpha():
        print("Key must contain letters only.")
        return


    with open(filename, "r") as file:
        ciphertext = file.read()


    decrypted_message = vigenere_decrypt(ciphertext, key)


    print("\n--- DECRYPTED MESSAGE ---")
    print(decrypted_message)





# ---------- MAIN MENU ----------
def main():
    print("Welcome to CipherWRL (Vigenère Edition)")


    while True:
        print("\n[0] Exit")
        print("[1] Create encrypted file")
        print("[2] Open and decrypt file")


        try:
            choice = int(input("Select option (0-2): "))
        except ValueError:
            print("Please enter a number.")
            continue


        if choice == 0:
            print("Goodbye.")
            break
        elif choice == 1:
            create_encrypted_file()
        elif choice == 2:
            decrypt_file()

        else:
            print("Invalid selection.")




if __name__ == "__main__":
    main()












