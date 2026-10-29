my_tuple = (1, 2, 3, 4, 'Hola', True, 2, 'Hi', 5, 4, 3, 2)
print(my_tuple)

# Es ordenada
# Son inmutables
# Permite duplicados
# Son indexadas, o sea que tienen un posición de 0 a n

# Tienen pocos métodos
print(my_tuple.count(2)) # => Cuenta cuantas veces aparece el 2

# .index
print(my_tuple.index('Hi')) # => Entrega el indice en el que está el elemento, si el elemento se repite trae el index de la primer aparición