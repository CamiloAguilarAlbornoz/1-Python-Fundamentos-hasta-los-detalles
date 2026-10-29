numbers_list = [1, 2, 3, 4, 5, 3]

# index(value) => Entrega el indice en donde está el valor buscado
print(numbers_list.index(2)) # => Da 1

# index(value, index_start, index_end) => Busca el valor e indica el indice siempre que esté entre el rango indicado (EL ULTIMO VALOR NO SE TOMA EN CUENTA)
print(numbers_list.index(3, 0, 3)) # => Da 2

# in => Indica si el valor está en la lista
print(2 in numbers_list) # => Da true

# count(value) => Se encarga de contar cuantas veces aparece el valor dentro de la lista
print(numbers_list.count(3))