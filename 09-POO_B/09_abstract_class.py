from abc import ABC, abstractmethod # Paquetes para crear clases y metodos abstractos

# Clase Abstracta
class Animal(ABC):
    
    @abstractmethod # Indica que el método es abstracto
    def sound(self):
        pass
    
    def sleep(self):
        return 'zzzz....'