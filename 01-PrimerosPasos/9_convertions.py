value = 100
#value = 100 + 'Hola' ==> Esta operación no está permitida, arroja error
type_value = type(value)
print(value)
print(type_value)

# Pasar Int a String
value = str(100) # Convierte el int en un string
type_value = type(value)
print(f'{value} fue convertido a un {type_value}')

'''
No se puede concatenar un string y un int, dos strings si se pueden concatenar
'''
# Pasar String a Int
value = int('100') # Convierte el string en un int
type_value = type(value)
print(value)
print(type_value)

# Pasar String a Float
value = float('100') # Convierte el string en un int
type_value = type(value)
print(value)
print(type_value)

# Pasar Int a Float
value = float(100) # Convierte el int en un float
type_value = type(value)
print(f'{value} fue convertido a un {type_value}')