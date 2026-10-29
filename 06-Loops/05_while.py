is_active = True
while is_active:
    print('\n1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División\n')
    
    option = int(input('Ingrese el número de la operación que desea realizar, (Cualquier número para salir): '))
    
    if option == 1:
        number_one = float(input('\nIngrese el primer numero: '))
        number_two = float(input('Ingrese el segundo numero: '))
        print(f'\nEl resultado de la suma es = {number_one + number_two}')
    elif option == 2:
        number_one = float(input('\nIngrese el primer numero: '))
        number_two = float(input('Ingrese el segundo numero: '))
        print(f'\nEl resultado de la resta es = {number_one - number_two}')
    elif option == 3:
        number_one = float(input('\nIngrese el primer numero: '))
        number_two = float(input('Ingrese el segundo numero: '))
        print(f'\nEl resultado de la multiplicación es = {number_one * number_two}')
    elif option == 4:
        number_one = float(input('\nIngrese el primer numero: '))
        number_two = float(input('Ingrese el segundo numero: '))
        if number_two != 0:
            print(f'\nEl resultado de la suma es = {number_one / number_two}')
        else: print('\nNo se puede dividir en 0')
    else: is_active = False
else: print('\nLa calculadora finalizó\n')
