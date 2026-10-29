def hello(greet='Buenas tardes', name='Invitado'):
    '''
    Esta es una función para devolver un saludo personalizado
    devuelve un print con el saludo
    '''
    print(f'{greet}, {name} ¿como estás?')

hello('Hola', 'Camilo')

def multiply(number_one: float, number_two: float) -> float: # Tipado de la función y sus parámetros
    '''
    Multiplica dos números y devuelve el resultado
    '''
    return number_one * number_two

print(multiply(4, 2))