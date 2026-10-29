# Conjuntos
my_set = {1, 2, 3}

#.add
my_set.add(6)
my_set.add(5)
print(my_set)

#.remove => Elimina un elemento pero da error si el elemento no existe
my_set.remove(2)
print(my_set)

# .discard => Funciona como el remove pero no marca error si el elemento no existe
my_set.discard(3)
print(my_set)

# .pop => Elimina un elemento al azar y lo devuelve
print(my_set.pop())
print(my_set)