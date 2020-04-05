import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

password_provided=input("What is your password?:\n")
password = password_provided.encode() # Convert to type bytes
#salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
print("password:  "+str(password))
print("salt:  "+str(salt))
print("key:  "+str(key))


message = "my deep dark secret".encode()
f=Fernet(key)
encrypted = f.encrypt(message)
print("encrypted message:  "+str(encrypted))

decrypted = f.decrypt(encrypted)
decrypted_decoded=decrypted.decode()
print("decrypted message in bytes:  "+str(encrypted))
print("decrypted and decoded message:  "+decrypted_decoded)