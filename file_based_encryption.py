from cryptography.fernet import Fernet
key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key)
file.close()

file = open('key.key','rb')
key=file.read()
file.close()


print(key)