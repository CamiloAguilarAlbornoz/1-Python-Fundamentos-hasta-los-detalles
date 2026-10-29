class Flyer:
    
    def fly(self):
        return 'Puedo volar'
    
    def do_something(self):
        return 'FlyFly'

class Swimmer:
    
    def swim(self):
        return 'Puedo nadar'
    
    def do_something(self):
        return 'SwimSwim'

class Duck(Flyer, Swimmer): # Hereda de multiples clases
    
    def quack(self):
        return 'Quack!'

donald = Duck()
print(donald.fly())
print(donald.swim())
print(donald.quack())
print(donald.do_something()) 
# Cuando una clase herda de dos clases que tienen el mismo método pero con resultados diferentes, 
# toma en cuenta el primero que encuentra. Esto pasa por el MRO (Method Resolution Order)
print(Duck.__mro__)