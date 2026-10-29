class Person:
    
    '''
    Esta es la forma en que se define un constructor
    
    self ==> Se refiere al objeto o clase como tal
    '''
    def __init__(self, name):
        self.name = name # Atributos de instancia
        self._energy = 100 # Si el atributo inicia con _ es porque es protegido
    
    def _waste_energy(self, quantity):
        self._energy -= quantity

person_one = Person('Camilo')
print(person_one.name)
person_one._waste_energy(20)
print(person_one._energy)