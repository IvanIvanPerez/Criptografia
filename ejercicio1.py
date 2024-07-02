#XOR de datos binarios
#Codificada por alguien usando libreria zip
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


#Ejercicio 1 apartado a
# K_desarrollo = B1EF2ACFE2BAEEFF 
# K_fichero = ? 
# K_final = K_desarrollo * K_fichero = 91BA13BA21AABB12

# Para obtener la clave del fichero properties que ha puesto el Key Manager, debemos hacer un XOR entra la clave de desarrollo y la clave final 

print("Solución apartado A: ")
print("Clave del fichero properties: ")
num11=0xB1EF2ACFE2BAEEFF
num22=0x91BA13BA21AABB12
num33=(hex(num11^num22))
print(num33[2:])

print("=========")

#Ejercicio 1 apartado b
# K_desarrollo = B1EF2ACFE2BAEEFF 
# K_fichero = B98A15BA31AEBB3F 
# K_final = K_desarrollo * K_fichero 

# Para obtener la clave final, debemos hacer un XOR entra la clave de desarrollo y la clave del fichero properties 

print("Solución apartado B: ")
print("Clave final en memoria: ")
num11=0xB1EF2ACFE2BAEEFF
num22=0xB98A15BA31AEBB3F
num33=(hex(num11^num22))
print(num33[2:])
