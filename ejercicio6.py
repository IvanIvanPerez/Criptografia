from Crypto.Hash import HMAC, SHA256, SHA512


mensaje_bytes = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.","UTF-8")
#Cogemos la clave del keystore
clave_bytes = bytes.fromhex('A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')

hmac_practica = HMAC.new(clave_bytes, msg=mensaje_bytes, digestmod=SHA256)
print("HMAC Práctica:", hmac_practica.hexdigest())



