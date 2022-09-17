from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f = Fernet(key)
with open('diabetes.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_diabetes.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

f = Fernet(key)

with open('enc_diabetes.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open ('dec_diabetes.csv', 'wb') as decrypted_file:
      decrypted_file.write(decrypted)