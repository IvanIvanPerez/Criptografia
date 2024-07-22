from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets




#Clave maestra -> A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72
#Salt: e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3

#salt = secrets.token_bytes(16)
#print(salt.hex())
salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")

#master_secret = secrets.token_bytes(64)
#print("maestra:", master_secret.hex())
master_secret = bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")

key1 = HKDF(master_secret, 32, salt, SHA512, 1)

print("Clave: ", key1.hex())
