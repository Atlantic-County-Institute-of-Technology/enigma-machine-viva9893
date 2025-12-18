# Enigma Machine
# author: Cesar Vivas
import os

# ENGLISH ALPHABET
UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# CIPHER
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
# Decryption
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



def main():
    print("You have entered CipherWRL")
    print("Create files with encrypted messages and open them using a key to unencrypt")
    print("If at any time you wish to exit, press '0'")

    while True:
        print("[-] 0. Exit")
        print("[-] 1. Encrypt a message and save to file")

        try:
            selection = int(input("Please select an option (0-1): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if selection == 0:
            print("Program is exiting.")
            break

        elif selection == 1:
            # get file name
            file_name = input("Enter file name (without extension): ").strip()
            file_name = file_name + ".txt"

            # check if file already exists
            if os.path.exists(file_name):
                print("Error: File already exists.")
                continue

            # get message and key
            message = input("Enter your message: ")
            key = input("Enter encryption key: ")

            # encrypt message
            encrypted_message = vigenere_encrypt(message, key)

            # write to file
            try:
                with open(file_name, "w") as file:
                    file.write(encrypted_message)
                print(f"Message encrypted and saved to '{file_name}'")
            except IOError:
                print("Error: Could not write to file.")
            while True:
                print("[-] 0. Exit\n"
                      "[-] 1. Encrypt New Message\n"
                      "[-] 2. Open File\n"
                      )

                try:
                    selection_0 = int(input("Please select an option(0-2) : "))
                except ValueError:
                    print("(Invalid input")
                    continue

                if selection_0 == 0:
                    print("Program is existing")
                    exit()
        #
                elif selection_0 == 1:  # takes you back to line line 85 to create file


        #
        #         elif selection_0 == 2:  # option 2 - apply a sorting algorithm.
        #             while True:
        #
        #                 print("[-] 1. bubble_sort\n"
        #                       "[-] 2. selection_sort\n"
        #                       "[-] 3. insertion_sort \n"
        #                       )
        #
        #                 try:
        #                     selection_2 = int(input("Please indicate an algorthim to sort the list (1-3) : "))
        #                 except ValueError:
        #                     print("(Invalid input")
        #                     continue
        #                 if selection_2 == 1:
        #                     sorted_list = bubble_sort(list[:])
        #                     bubble_count += 1
        #
        #                 elif selection_2 == 2:
        #                     sorted_list = selection_sort(list[:])
        #                     selection_count += 1
        #
        #                 elif selection_2 == 3:
        #                     sorted_list = insertion_sort(list[:])
        #                     insertion_count += 1
        #
        #                 else:
        #                     print("invalid choice")
        #                     continue
        #                 print(f"old list = {list} ")
        #                 print(f"sorted list = {sorted_list}")
        #                 break
        #                 # access saved data, such as the  number of sorts and the total number of sorting actions
        #         elif selection_0 == 3:
        #
        #
        # else:
        #     print("Invalid option. Please choose 0 or 1.")

if __name__ == "__main__":
    main()

