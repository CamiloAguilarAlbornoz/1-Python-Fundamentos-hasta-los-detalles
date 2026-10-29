# in y not in
'''
Permite indicar si algo pertenece o no a algo

por ejemplo un numero pertenece a un grupo de numeros
'''

print(9 in range(1, 10)) # range trae un listado de 10 números, en este caso del 0 al 9

fruits = ['manzana', 'banana', 'fresa']
print('fresa' in fruits) # Da true
print('mango' not in fruits) # Da true porque mango no está en las frutas

sentence = 'Soy programador en python, golang y php'
print('python' in sentence)
print('mongo' in sentence)