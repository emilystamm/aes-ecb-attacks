# aes_ecb_password_attack.py

from Crypto.Cipher import AES
import sys
import binascii
from aes_ecb_password_oracle import encrypt, cipher, oracle
from words_list import words_list_fn

wordct = ""

# main
# -------------------------------
def main():
    # Dictionary we will fill with key = ciphertext, value = plaintext
    D = {}
    word_list = words_list_fn()
    block_size = 16
    print("\n\n\n")

    # Encrcrypt and add ciphertext,plaintext pair
    # to dictionary for each word in word_list
    for word in word_list:
        try:
            cipher.block_size= block_size
            chosen = "Password: " + word 
            print("\nPlaintext: ", chosen)
            ct = oracle(chosen, block_size)
            print("Ciphertext: ", hex(ct), "\n")
   
            # Add ciphertext, plaintext pair to dictionary
            D[str(hex(ct))] = word

        except ValueError:
            print("Invalid. ")

    chosen = input("\nEnter encrypt, decrypt, or exit: \n")
    while chosen != "exit":

        # If input 'encrypt' - check if word is in encrypted dictionary
        # and if it is, return encrypted value
        # if not, encrypt it add it to dictionary 
        while chosen != 'exit' and chosen == 'encrypt':
            chosen = input("\nEnter password: \n")
            chosen = "Password: " + chosen
            print("Plaintext:  ", chosen)
            padded = getPadding(chosen, block_size)
            print("Plaintext with padding:  ", padded)
            ct = oracle(chosen, block_size)
            print("Encrypted:  ", str(hex(ct)), "\n\n")
            if str(hex(ct)) not in D.keys():
                print("Was not in dictionary, but adding now")
                D[str(hex(ct))] = chosen

        # If input 'decrypt' - check dictionary to see if it has that ciphertext
        # and if it does, return corresponding password
        while chosen != 'exit' and chosen == 'decrypt':
            chosen = input("\nEnter encrypted value: \n")
            print("Encrypted:  ", chosen)
            if chosen in D.keys():
                print("\nSucess!\nThis encrypted value is recorded in our dictionary\n")
                print(D[chosen])
            else: 
                print("Not in our dictionary :/\n")

        # Continue until type exit
        chosen = input("\nEnter encrypt, decrypt, or exit: \n")

    exit("\nUsage: %s plaintext" % sys.argv[0])

# Hex - encoding
# -------------------------------
def hex(elt): return binascii.hexlify(elt)

# Split up word
# -------------------------------
def split_len(seq, length): return [seq[i:i+length] for i in range(0, len(seq), length)]

# Pad secret
# -------------------------------
def getPadding(secret, block_size):
    pl = len(secret)
    mod = pl % block_size
    if mod != 0:
        padding = block_size - mod
        secret += str(mod % 8) * padding
    return secret


if __name__ == "__main__":
    main()
    


