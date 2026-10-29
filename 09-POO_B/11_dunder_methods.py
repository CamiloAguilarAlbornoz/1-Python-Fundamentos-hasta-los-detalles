# dunder => Metodos con doble guion al inicio y al final
class Person:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self): # Util para que al imprimir la instancia no muestre la dirección en memoría sino que se muestre un string personalizado
        return f'Hola, soy {self.name}'
    
    def __len__(self): # Util para implementar el método len() sobre la instancia
        return len(self.name)

person = Person('Camilo')
print(person)
print(len(person))