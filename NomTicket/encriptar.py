import random
from werkzeug.security import generate_password_hash
from django.contrib.auth.hashers import make_password
import string

letras = string.ascii_letters
clave = "1212"
numeros = string.digits
puntuacion = string.punctuation
base = letras+numeros+puntuacion
longitud = 10
muestra = generate_password_hash(clave)
print (muestra)

#for _ in range(2):
#    muestra = random.sample(clave,longitud)
#    password = "".join(muestra)
#    password_encriptado = generate_password_hash(password)
#    print(password)
#    print(password_encriptado)
    #print("{} => {}".format(password,password_encriptado))
    


