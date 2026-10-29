# Es para tener control de toda la lógica o flujo que se quiere plantear

# Ejemplo

age = int(input('Introduce tu edad: '))
if age < 0:
    print('La edad no puede ser negativa')
elif age <= 12:
    print('Eres un infante')
elif age <= 17:
    print('Eres un adolescente')
elif age <= 64:
    print('Eres un adulto')
else:
    print('Ere un adulto mayor')