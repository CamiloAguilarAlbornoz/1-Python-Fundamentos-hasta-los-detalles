class Animal:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sound(self) -> str:
        return f'{self.name} hace un sonido'
    
    def info(self):
        return f'Soy {self.name} y tengo {self.age} años'

class Dog(Animal): # Indica que la clase Dog hereda de la clase Animal
    
    def __init__(self, name, age, breed):
        super().__init__(name, age) # Así envía los datos a la clase padre
        self.breed = breed
    
    def sound(self):
        animal_sound = super().sound()
        return f'{animal_sound} y soy {self.name} y digo guau'
    
    def info(self):
        return f'{super().info()} además mi raza es {self.breed}'

class Cat(Animal): # Indica que la clase Cat hereda de la clase Animal
    
    def sound(self):
        super().sound()
        animal_sound = super().sound()
        return f'{animal_sound} y {self.name} dice miau miau'

firulais = Dog('Firulais', 5, 'Snauser')
print(firulais.sound())
print(firulais.info())