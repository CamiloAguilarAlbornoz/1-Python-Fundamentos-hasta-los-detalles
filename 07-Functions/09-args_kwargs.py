'''
 *args   ==> Permite que la función reciba n argumentos
**kwargs ==> Permite que cuando la función reciba argumentos multiples, se guarden en un diccionario

*args vs **kwargs ==> en args no es necesario definir un nombre de variable en kwargs si

'''
def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    data_to_shwow = ''
    for item in kwargs.values():
        data_to_shwow += f'{item} =>'
    print(data_to_shwow)
    return sum(args)

print(big_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name='Camilo', age=29, city='Tunja - Simijaca'))