# aes_ecb_password_oracle.py

from Crypto.Cipher import AES
# len of key - 16 chars
key = "deadbeefc2fecode"
cipher = AES.new(key, AES.MODE_ECB)
import time
import binascii

# len of key - 16 chars
key = "rAndom1234567key"

# Encrypt/Decrypt functions 
# -------------------------------
def encrypt(secret): return cipher.encrypt(secret)

def decrypt(secret): return cipher.decrypt(secret)

# Pad secret
# -------------------------------
def getPadding(secret, block_size):
    pl = len(secret)
    mod = pl % block_size
    if mod != 0:
        padding = block_size - mod
        secret += str(mod % 8) * padding
    return secret

# Hex - encoding
# -------------------------------
def byte_to_hex(elt): return binascii.hexlify(elt)

# Oracle responsible for encryption
# -------------------------------
def oracle(chosen, block_size):
    secret = "%s" % chosen # target to decrypt
    secret = getPadding(secret, block_size)
    print("Target: ", secret)
    ct = encrypt(secret)
    return ct