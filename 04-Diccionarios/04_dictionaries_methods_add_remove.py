user = {
    'name': 'Camilo',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# .copy => Copia el diccionario a una variable
user_copy = user.copy()
user_copy['age'] = 30
print(f'\nDiccionario original {user}\nCopia del diccionario {user_copy}')

# .pop(key) => Elimina el elemento indicado por la llave
user.pop('age')
print(f'\nDiccionario sin edad {user}')

# .popitem() => Elimina el ultimo elemento del diccionario
user.popitem()
print(f'\nDiccionario sin el ultimo elemento {user}')

# .update() => Permite actualizar el diccionario, si se coloca un valor inexistente, lo agrega al diccionario
user.update({'name': 'Camilo Aguilar'})
print(f'\nDiccionario actualizado {user}')

# .append() =>
user['skills'] = user.get('skills', [])
user['skills'].append('Python')
print(f'\nDiccionario modificado con append {user}\n')