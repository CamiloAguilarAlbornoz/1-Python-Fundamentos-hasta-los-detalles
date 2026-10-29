class Animal:
    
    def __init__(self, name):
        self.name = name
    
    def sleep(self) -> str:
        return f'{self.name} está durmiendo'

class Dog(Animal): # Indica que la clase Dog hereda de la clase Animal
    
    def dog_sound(self):
        return f'{self.name} dice guau guau'

class Cat(Animal): # Indica que la clase Cat hereda de la clase Animal
    
    def cat_sound(self):
        return f'{self.name} dice miau miau'

firulais = Dog('firulais')
print(firulais.sleep())
print(firulais.dog_sound())

malva = Cat('malva')
print(malva.sleep())
print(malva.cat_sound())