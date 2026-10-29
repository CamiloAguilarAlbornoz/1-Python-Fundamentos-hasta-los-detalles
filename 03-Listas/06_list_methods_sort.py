letters = ['a', 'z', 'b', 'g', 'c', 'm', 'd', 'o', 'e']

# sorted() => Ordena la lista, con la diferencia de que entrega un nuevo arreglo para no modificar el original
new_letters = sorted(letters)
print(f'Lista original {letters}')
print(f'Nueva lista ordenada {new_letters}')

# Sin usar sorted()
new_letters_two = letters[::]
new_letters_two.sort()
print(f'Nueva lista ordenada {new_letters_two} sin usar sorted()')

# sort() => Se encarga de ordenar la lista en el caso de letras en orden alfabético, en números de menor a mayor
letters.sort()
print(f'Lista ordenada {letters}')

# Reverse => Se encarga de voltear la lista
letters.reverse()
print(f'Invierte la lista {letters}')