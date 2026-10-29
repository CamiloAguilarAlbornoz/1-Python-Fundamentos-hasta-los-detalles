'''
with es una palabra clave para que abra el archivo y de forma
automática se cierre, Todo lo relacionado al archivo debe estar en el bloque
de código

el mode = 'r' indica que el archivo se abre en modo lectura
'''
with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())

'''
el mode = 'w' indica que el archivo se abre en modo escritura

el write sustituye todo el contenido del archivo, y elimina toda la info

write crea el archivo si este no existe
'''
with open('archivo.txt', mode='w') as my_file:
    text = my_file.write('>:P')
    
'''
r+ indica que el archivo funciona tanto para lectura como escritura
'''
with open('test.txt', mode='r+') as my_file:
    print(my_file.readlines())
    text = my_file.write('Hola Mundo')

'''
Se encarga de concatenar el texto que tiene el archivo con el nuevo
'''
with open('test2.txt', mode='a') as my_file:
    text = my_file.write('123')
    print(text)