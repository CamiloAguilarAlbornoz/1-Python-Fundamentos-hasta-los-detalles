from abc import ABC, abstractmethod # Paquetes para crear clases y metodos abstractos

# Clase Abstracta
class Animal(ABC):
    
    @abstractmethod # Indica que el método es abstracto
    def sound(self) -> str:
        pass
    
    def sleep(self):
        return 'zzzz....'

class Dog(Animal):
    
    def sound(self) -> str:
        return 'Woof Woof'

class Cat(Animal):
    
    def sound(self) -> str:
        return 'Miew Miew'

firulais = Dog()
print(firulais.sound())
michifu = Cat()
print(michifu.sound())