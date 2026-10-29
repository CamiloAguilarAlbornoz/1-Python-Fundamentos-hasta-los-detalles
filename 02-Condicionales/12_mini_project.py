name = input('Por favor ingrese su nombre: ')
years_of_experience = int(input('Por favor ingrese cuantos años de experiencia tiene para el puesto: '))
habilities = input('Por favor ingrese las tecnologías y lenguajes de programación que maneja separado por ,: ')
habilities = habilities.lower().split(',')

# Evaluaciones
if 'python' in habilities and 'django' in habilities:
    if years_of_experience >= 3:
        print(f'Felicidades {name} eres un candidato optimo')
    elif years_of_experience >= 1:
        print(f'Felicidades {name} eres un buen candidato')
    else:
        print(f'Felicidades {name} eres un posible candidato')
else:
    print(f'Lo lamentamos {name} no eres un candidato óptimo, pero tu cv se guardará, no nos llames, nosotros te llamamos')
