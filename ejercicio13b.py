import ed25519
from Crypto.Hash import SHA256

#Firmamos primero.
#Clave privada porque firmamos.
privatekey = open("ed25519-priv","rb").read()

#Creo un objeto para firmar y le paso la clave privada
signedKey = ed25519.SigningKey(privatekey)

msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
#El hash de aqui es un objeto
hash=SHA256.new(msg)

#Firmamos un hash. 
signature = signedKey.sign(bytes.fromhex(hash.hexdigest()), encoding='hex')
print("Firma Generada (64 bytes):", signature)


print("Proceso de validar la firma será:")

publickey = open("ed25519-publ","rb").read()

try:
    verifyKey = ed25519.VerifyingKey(publickey.hex(),encoding="hex")
    verifyKey.verify(signature, bytes.fromhex(hash.hexdigest()), encoding='hex')
    print("La firma es válida")
except:
    print("Firma inválida!")