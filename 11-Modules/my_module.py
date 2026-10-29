def greet():
    print('Hola desde Modulo')

if __name__ == '__main__': # Solo se encuta si se llama este archivo dado que con este código my_module se interpreta como el principal
    print('Este modulo se está ejecutando directamente')
    greet()

print('Este es el archivo pricipal')