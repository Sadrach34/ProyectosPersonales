import random
import string

def generar_contraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + "*@!$|"
    contraseña = ''.join(random.choices(caracteres, k=longitud))
    return contraseña

# Ejemplo de uso
print("Contraseña generada:", generar_contraseña())
