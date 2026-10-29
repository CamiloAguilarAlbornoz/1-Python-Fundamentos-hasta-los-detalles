try:
    with open('otro_archivo.txt') as file:
        content = file.read()
except FileNotFoundError:
    print(f'El archivo no existe')

try:
    with open('sinpermisos.txt') as file:
        content = file.read()
        print(content)
except PermissionError:
    print(f'El archivo no tiene permisos de lectura')