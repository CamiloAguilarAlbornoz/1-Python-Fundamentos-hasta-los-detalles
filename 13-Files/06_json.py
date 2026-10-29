import json

users = {
    'Nombre': 'Camilo',
    'edad': 29,
    'activo': True
}

''' Escribe el JSON '''
with open('data.json', mode='w') as file:
    json.dump(users, file, indent=4)

''' Lee el JSON '''
with open('data.json', mode='r') as file:
    data_read = json.load(file)
    print(data_read)