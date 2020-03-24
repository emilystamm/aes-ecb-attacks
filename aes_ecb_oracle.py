# aes_ecb_oracle.py

from Crypto.Cipher import AES
import binascii
import time
from Crypto.Random import get_random_bytes

# Set Variables 
# -------------------------------
# keey that will be used for encryption (16 bytes)
keey = get_random_bytes(16)
print("Keey = ", keey)
# tooken or secret information (<= 16 chars)
tooken = "VERYsecrettook1" 

# Cipher
# -------------------------------
cipher = AES.new(keey, AES.MODE_ECB)

# Encrypt a string
# -------------------------------
def encrypt(message): 
	return cipher.encrypt(message)

# Encrypt a message including the string target
#	display everything oracle knows if display = True
# -------------------------------
def oracle(target, display = False, see_oracle = False, timing = False):
	message = getPadding("data=" + target + ",tooken=" + tooken)
	message_encoded = message.encode()
	encrypted = encrypt(message_encoded)
	if display:
		if timing: time.sleep(.05)
		disp(message, target, encrypted, see_oracle)
	encrypted_decoded = byte_to_hex(encrypted)
	print("Encrypted decoded", encrypted_decoded)
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
		print("Secret we don't know:", tooken)
		print("\tEncrypting with AES-ECB.... \n\tkeey =", keey)
	else: print("Message Split", message[0:16], " ", message[16:32], " ", 16 * "?", " ", 16 * "?", " ", "?" * 16, " ", "?" *16, " ")
	print("Encrypted:", byte_to_hex(encrypted), "\n\n")
