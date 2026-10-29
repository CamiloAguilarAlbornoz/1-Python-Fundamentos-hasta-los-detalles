inventory = {
    'chocolate': 10,
    'gomitas': 5,
    'paleta': 8,
    'chicle': 2,
    'mexicano': 8,
    'galleta': 12
}

cart = []

print('\n********************************************')
print('¡Bienvenido a la tienda de dulces, DevCandy!')

option = ''
while (option.lower() != 'salir'):
    print('********************************************\n')
    for key, value in inventory.items():
        print(f'{key} ${value}.')
    option = input('\nIngrese el dulce que desea agregar al carrito (ingrese salir para finalizar la compra): ')
    if (option in inventory):
        cart.append(option)
else:
    print('\n********************************************\n')
    total_to_pay = 0
    print('Dulces que compró\n')
    for candy in cart:
        print(f'{candy} ${inventory[candy]}.')
        total_to_pay += inventory[candy]
    print(f'\nEl precio a pagar es {total_to_pay}\n')