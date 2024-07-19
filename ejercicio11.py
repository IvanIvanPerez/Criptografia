from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import os
my_path = os.path.abspath(os.getcwd())

#fichero_pub = my_path + "/public-rsa.pem"
fichero_pub = my_path + "/clavepublica-RSA_desc_oaep.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())


mensaje = bytes.fromhex("45 73 74 6f 20 65 73 20 75 6e 20 6d 65 6e 73 61 6a 65 20 64 65 20 70 72 75 65 62 61")

encryptor = PKCS1_OAEP.new(keypub,SHA256)
encrypted = encryptor.encrypt(mensaje)

print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")

