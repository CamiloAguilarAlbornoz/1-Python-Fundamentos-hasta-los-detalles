numbers = [1, 2, 3, 4, 5]

# Iterables => son los iterables, listas, diccionarios, sets, tuplas y clases personalizadas
# Iterator => Es un objeto que recuerda su posición
iterator = iter(numbers) # Convierte la lista iterable en un iterador
print(next(iterator)) # Con next accede a cada elemento de la lista

user = {
    'name': 'Camilo',
    'age': 22,
    'can_swim': False
}

for item in user.items():
    key, value = item
    print(f'{key} => {value}')