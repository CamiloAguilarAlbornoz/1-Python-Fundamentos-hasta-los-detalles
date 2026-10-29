'''
Las llaves son inmutables SIEMPRE
'''

user = {
    'name': 'Camilo',
    'age': 29,
    'email': 'camilo@email.com',
    (1, 2, 3): [1, 2, 3]
}

user['name'] = 'Camilo Andrés Aguilar Albornoz'
user['age'] = 30
user['country'] = 'Colombia'

print(user)
print(f'\n{user[(1, 2, 3)]}')