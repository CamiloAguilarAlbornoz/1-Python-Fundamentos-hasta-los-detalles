import csv

'''
newline para que no cree espacios en blanco
'''
with open('datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Edad'])
    writer.writerow(['Silvana', 28])
    writer.writerow(['Mayerly', 28])
    writer.writerow(['Dayana', 29])
    writer.writerow(['Carolina', 27])

''' Para leer el documento '''
with open('datos.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)