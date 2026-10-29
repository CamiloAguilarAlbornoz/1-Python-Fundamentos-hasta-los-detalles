def divide_numbers():
    try:
        number_a = int(input('Ingresa el numerador : '))
        number_b = int(input('Ingresa el denominador : '))
        result = number_a / number_b
    except ZeroDivisionError:
        return f'No se puede dividir entre 0, el denominador que ingresaste fue {number_b}'
    except ValueError:
        return f'Los datos a ingresar deben ser numéricos'
    else:
        return result # Si no se presenta ninguna excepcion
    finally: # Se ejecuta tanto si hubo como si no hubo error
        print('Gracias por usar la calculadora')

print(divide_numbers())

# Else - Finally

