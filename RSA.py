import csv
import rsa
import math
import pandas as pd

data = pd.read_csv('diabetes.csv')
print(data)


def generateKeys():
    (publickey, privateKey) = rsa.newkeys(1024)
    with open('publicKey.pem', 'wb') as p:
        p.write(publickey.save_pkcs1('PEM'))
    with open('privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))


print(generateKeys())


def loadKeys():
    with open('publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey
print(loadKeys())

'''
def encrypt(data, key):
    return rsa.encrypt(data.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False


def sign(data, key):
    return rsa.sign(data.encde('ascii'), key)


def verify(data, signature, key):
    try:
        return rsa.verify(data.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False


generateKeys()
publicKey, privateKey = loadKeys()

ciphertext = encrypt(data, publicKey)
signature = sign(data, privateKey)
text = decrypt(ciphertext, privateKey)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')

if text:
    print(f'Data: {text}')
else:
    print(f'Unable to decrypt the data.')

if verify(text, signature, publicKey):
    print('Successfully verified signature')
else:
    print('The message signature could not be verified')
'''