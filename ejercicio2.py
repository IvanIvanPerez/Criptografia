
   
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


#Clave: A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72
#Algoritmo: AES/CBC/PKCS7
#IV: 00000000000000000000000000000000
#Texto cifrado: TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4US t3aB/i50nvvJbBiG+le1ZhpR84oI= 

clave_bytes = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')
texto_cifrado_bytes= b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")
iv_bytes = bytes.fromhex('00000000000000000000000000000000')

#Descifrado con PKCS7
cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")
#mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)


#Descifrado con x923
cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
mensaje_des_bytes_x923 = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="x923")
#mensaje_des_bytes_x923 = cipher.decrypt(texto_cifrado_bytes)


print("El texto en claro con PKCS7 es: ", mensaje_des_bytes.decode("utf-8"))
print(mensaje_des_bytes.hex())
print("El texto en claro con x923 es: ", mensaje_des_bytes_x923.decode("utf-8"))
print(mensaje_des_bytes_x923.hex())



