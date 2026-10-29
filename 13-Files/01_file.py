my_file = open('test.txt') # Abrir un archivo, NO LO GENERA
print(my_file.read()) # Lee lo que tenga el archivo, solo lo muestra una vez, sin importar cuantas veces se ejecute el print

# seek
my_file.seek(0) # Permite situarse en la posición en bytes del archivo, de esa forma se puede imprimir
print(f'\n{my_file.read()}')
'''
Solo se puede imprimir una vez porque read() recorre todo el archivo, si se envía otro print
agregará un espacio en blanco, seek() situa al interprete en el byte que se le indique y se ejecuta
read() nuevamente leerá el archivo a partir de ese byte, permitiendo que el archivo se lea nuevamente
'''

# readline
my_file.seek(0)
print(f'\n{my_file.readline()}') # Se encarga de leer una línea del archivo

# readlines
print(f'\n{my_file.readlines()}') # Me entrega las líneas sobrantes, o sea las que readline() no leyó

my_file.close() # Cerrar un archivo