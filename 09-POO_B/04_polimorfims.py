class Animal:
    
    def make_sound(self) -> str:
        return f'Sonido de animal'

class Dog(Animal):
    
    def make_sound(self) -> str:
        return f'Woof Woof!'

class Cat(Animal):
    
    def make_sound(self) -> str:
        return f'Meaw Meaw!'

def make_noise(animal):
    if isinstance(animal, Animal): # Permite controlar si el objeto es instancia de Animal, o si hereda de Animal
        print(animal.make_sound())
    else:
        print('Esto no es un animal')

make_noise(Dog())
make_noise(Cat())
make_noise('Hola Mundo')