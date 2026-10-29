# Default parameter
def hello(greet='Buenas tardes', name='Invitado'):
    print(f'{greet}, {name} ¿como estás?')

# Argumentos
hello('Hola', 'Camilo')
hello()
hello('Hola')
hello(name='Camilo')