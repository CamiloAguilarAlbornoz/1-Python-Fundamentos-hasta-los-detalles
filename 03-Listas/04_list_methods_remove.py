numbers_list = [1, 2, 3, 4, 5]

print(f'Lista original {numbers_list}')

# pop() => Elimina el último elemento de una lista
numbers_list.pop()
print(f'Lista tras eliminar el ultimo elemento {numbers_list}')

# pop(index) => Elimina el elemento indicado por parametro
numbers_list.pop(1)
print(f'Lista tras eliminar elemento indicado en el index 1 {numbers_list}')

# remove(value) => Recibe el valor que se desea eliminar, NO EL INDEX COMO EN pop(index), si ese elemento está repetido elimina solo su primer aparición
numbers_list.remove(3)
print(f'Lista tras eliminar el 3 {numbers_list}')

# clear() => Elimina toda la lsita
numbers_list.clear()
print(f'Lista eliminada {numbers_list}')