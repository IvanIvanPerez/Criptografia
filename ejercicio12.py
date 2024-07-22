import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


plaintext_bytes = bytes("He descubierto el error y no volveré a hacerlo mal","UTF-8")
clave_bytes = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = b64decode('9Yccn/f5nJJhAt2S')

datos_asociados_bytes = bytes("","UTF-8")
cipher = AES.new(clave_bytes, AES.MODE_GCM,nonce=nonce)

cipher.update(datos_asociados_bytes)
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(plaintext_bytes)

print("CipherText_Hex: ", texto_cifrado_bytes.hex())
print("CipherText_B64: ", b64encode(texto_cifrado_bytes).decode())
print("Tag:", tag.hex())

