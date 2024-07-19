import hashlib


# initiating the "s" object to use the
# sha3_256 algorithm from the hashlib module.
s = hashlib.sha3_256()

# will output the name of the hashing algorithm currently in use.
print(s.name)

# will output the Digest-Size of the hashing algorithm being used.
print(s.digest_size)

# providing the input to the hashing algorithm.
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))


print(s.hexdigest())


import hashlib
from Crypto.Hash import keccak

m = hashlib.md5()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8")) #12b66b74dda1f16030efb0505fdf70c3
print("md5:    " + m.digest().hex())


m = hashlib.sha1()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA1:   " + m.digest().hex())

m = hashlib.sha256()  
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8")) #8a261ce1a2b1d6ba1972ec971ec0f401ca69df46bbe8a8c977f764bc972920d2
print("SHA256: " + m.digest().hex())

m = hashlib.sha512()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print("SHA512: " + m.digest().hex())

m = hashlib.sha3_256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","UTF-8"))
print("SHA3-256:", m.digest().hex())

m = hashlib.sha3_256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))
print("SHA3-256:", m.digest().hex())