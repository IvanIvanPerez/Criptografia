from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_mensaje = b64decode('9Yccn/f5nJJhAt2S')
print('nonce  = ', nonce_mensaje.hex())

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado = cipher.encrypt(textoPlano)
print('Mensaje cifrado en HEX = ', texto_cifrado.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode())


#Descifrado...
decipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
plaintext = decipher.decrypt(texto_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))


