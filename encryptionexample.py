from cryptography.fernet import Fernet as Fer

"""
Basic encryption example
"""

# Generates a byte-string encryption key
key = Fer.generate_key()

print(f"key: {key}\n")

# Stores key in memory
f = Fer(key)

# String that we want to encrypt
# String must be a byte type string, can't encrypt UTF-8/UTF-16 (Unicode)
encryptedString = f.encrypt(b"Hello World!")

print(f"encrypted string: {encryptedString}\n")

# Take the key from memory and decrypt the message
decryptedString = f.decrypt(encryptedString)

print(f"decrypted string: {decryptedString}")
