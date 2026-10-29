x = [1, 2, 3, 4, 5]

print(type(x)) # Indica el tipo del objeto x
print('\n*******************************************************************************************\n')
print(dir(x)) # Entrega la lista de métodos y atributos del objeto x
print('\n*******************************************************************************************\n')
print(hasattr(x, '__len__')) # Indica si el atributo ingresado por parametro existe en el objeto x
print('\n*******************************************************************************************\n')
print(getattr(x, 'append')) # Indica la referencia en hexadecimal del método append del objeto x
print('\n*******************************************************************************************\n')
print(callable(x.append)) # Indica que el método append si se puede ejecutar
print('\n*******************************************************************************************\n')
print(id(x)) # Indica la dirección en memoria del objeto en decimal
print('\n*******************************************************************************************\n')