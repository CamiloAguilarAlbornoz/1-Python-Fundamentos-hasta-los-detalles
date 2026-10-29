# Métodos de adición
numbers_list = [1, 2, 3, 4, 5]

# append => Agrega un valor al final de la lista
print(f'Lista original = {numbers_list}')
numbers_list.append(100)
print(f'Lista despues de agregarle algo {numbers_list}')
numbers_list.append(200)
print(f'Lista despues de agregarle algo {numbers_list}')

# Insert => Agrega un valor en la posición indicada, NO SUSTITIYE EN VALOR DE UNA POSICIÓN PREVIA SINO QUE LA CAMBIA DE LUGAR A LA DERECHA
numbers_list.insert(1, 300)
print(f'Lista despues de agregarle algo {numbers_list}')
numbers_list.insert(3, 400)
print(f'Lista despues de agregarle algo {numbers_list}')

# Extends => Permite agregar listas dentro de otra lista, justo al final
numbers_list.extend([11, 22, 33])
print(f'Lista despues de agregarle algo {numbers_list}')