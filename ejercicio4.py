import jwt


#Generamos jwt. Necesitaremos el Payload. {"felipe": "Keepcoding"}
#Necesitamos la clave: "KeepCoding"
#Algoritmo de firma o mac.

encoded_jwt = jwt.encode({"usuario": "Don Pepito de los palotes",
  "rol": "isAdmin",
  "iat": 1667933533
}, "Con KeepCoding aprendemos", algorithm="HS256")

print(encoded_jwt)

decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")

print(decode_jwt)