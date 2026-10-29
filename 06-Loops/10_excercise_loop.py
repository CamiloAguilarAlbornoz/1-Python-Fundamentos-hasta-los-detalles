shopping_cart = ['Laptop', 'Vaso', 'Cafe', 'Audifonos']
option = ''
while option != '7':
    print('***********************************')
    print('Opciones')
    print('1. Agregar producto')
    print('2. Eliminar producto')
    print('3. Mostrar la lista ordenada')
    print('4. Buscar producto')
    print('5. Contar productos del carrito')
    print('6. Vaciar el carrito')
    print('7. Salir')
    print('***********************************')
    option = input('Elige una opción del (1 - 6) : ')

    if option == '1':
        new_product = input('Agrega un nuevo producto al carrito: ')
        if new_product not in shopping_cart:
            shopping_cart.append(new_product)
        else:
            print('\n El producto ya está en el carrito\n')
    elif option == '2':
        product_to_remove = input('Ingrese el producto que desea eliminar: ')
        if product_to_remove in shopping_cart:
            shopping_cart.remove(product_to_remove)
        else:
            print('\nEl producto no existe')
    elif option == '3':
        if len(shopping_cart) > 0:
            order_shopping_cart = sorted(shopping_cart)
            print(f'\nLista de compras ordenada \n{order_shopping_cart}\n')
        else: print('\nLa lsita no tiene elementos\n')
    elif option == '4':
        product_to_find = input('Ingrese el producto que desea buscar: ')
        if product_to_find in shopping_cart:
            print(f'\nProducto encontrado es = {shopping_cart[shopping_cart.index(product_to_find)]}\n')
        else: print('\nEl producto no existe\n')
    elif option == '5':
        print(f'\nLa cantidad de productos en el carrito es {len(shopping_cart)}\n')
    elif option == '6':
        shopping_cart.clear()
    else: print('Opción no valida')
else: print('\nFinalizo la compra, tenga un excelente día\n')