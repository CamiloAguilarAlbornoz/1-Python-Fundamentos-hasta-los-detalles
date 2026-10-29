# letras         = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numeros        = "0123456789"
# simbolos       = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
# caracteres     = letras + numeros + simbolos
# Formula simple = (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Salida: &D^#23SN

import random
import string

def generator_password(longitud):
    characters = f'{string.ascii_letters}{string.digits}{string.punctuation}'
    counter_of_characters = 0
    new_password = ''
    while (counter_of_characters < longitud):
        item = random.randint(0, len(characters))
        new_password += characters[item]
        counter_of_characters += 1
    return new_password

longitud = int(input('Ingresa la longitud de la contraseña: '))
new_password = generator_password(longitud)
print(f'Tu contraseña segura es = {new_password}')