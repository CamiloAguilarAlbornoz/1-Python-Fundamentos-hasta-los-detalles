a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] # => Asigna cada valor de la lsita a cada variable, si se agrega una nueva variable despues del *, guardara el ultimo elemento y seguirá hacia atrás, la desempaqueta, * agrega el resto del arreglo a un array nuevo llamado other
print(a) # => 1
print(b) # => 2
print(c) # => 3
print(other) # => [4, 5, 6, 7, 8]
print(d) # => 9