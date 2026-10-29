list_one = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1]
tuple_one = tuple(list_one) # Convierte la lista list_one a una tupla
set_one = set(tuple_one) # Convierte la tupla tuple_one a un set

list_tuple = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(list_tuple) # Convierte a lista de tuplas a un diccionario

print(f'\nLista original {list_one}')
print(f'Lista convertida en tupla {tuple_one}')
print(f'Tupla convertida en set {set_one}')
print(f'Lista de Tuplas convertida a diccionario {dictionary}\n')