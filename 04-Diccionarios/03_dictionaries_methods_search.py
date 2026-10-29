user = {
    'name': 'Camilo',
    'age': 29,
    'greet': 'Hola Mundo',
    'numbers': [1, 2, 3]
}

# get => Permite obtener un valor de acuerdo a la llave que reciba
print(user.get('name'))

# in => Solo busca en las llaves
print('greet' in user)

# Para que busque por los valores
print(29 in user.values())

# items => trae un listado total del diccionario
print(user.items())