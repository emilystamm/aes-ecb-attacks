# aes_ecb_oracle.py

from Crypto.Cipher import AES
import binascii
import time


# Set Variables 
# -------------------------------
# Key that will be used for encryption (16 chars)
key = "rAndom1234567key"
# Token or secret information (<= 16 chars)
token = "secrettoken1234" 

# Cipher
# -------------------------------
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt a string
# -------------------------------
def encrypt(message): return cipher.encrypt(message)

# Encrypt a message including the string target
#	display everything oracle knows if display = True
# -------------------------------
def oracle(target, display = False, see_oracle = False, timing = False):
	message = getPadding("data=" + target + ",token=" + token)
	encrypted = encrypt(message)
	if display:
		if timing: time.sleep(.05)
		disp(message, target, encrypted, see_oracle)
	return encrypted 


# Padding
# -------------------------------
def getPadding(secret):
    pl = len(secret)
    mod = pl % 16
    if mod != 0:
        padding = 16 - mod
        secret += 'X' * padding
    return secret

# For display purposes
# -------------------------------

def byte_to_hex(elt): return binascii.hexlify(elt)

def disp(message, target, encrypted, see_oracle):
	if see_oracle: print("\nMessage to encrypt: ", message)
	else: print("\nMessage to encrypt: ?")
	print("Target given: ", target)
	if see_oracle:
		print("Message Split", message[0:16], " ", message[16:32], " ", message[32:48], " ", message[48:64], " ", message[64:80], " ", message[80:96], " ")
		print("Secret we don't know:", token)
		print("\tEncrypting with AES-ECB.... \n\tkey =", key)
	else: print("Message Split", message[0:16], " ", message[16:32], " ", 16 * "?", " ", 16 * "?", " ", "?" * 16, " ", "?" *16, " ")
	print("Encrypted:", byte_to_hex(encrypted), "\n\n")
