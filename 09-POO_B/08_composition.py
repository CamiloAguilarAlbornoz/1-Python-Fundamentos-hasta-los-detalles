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

class Duck:
    
    def __init__(self):
        self.flyer = Flyer()
        self.swimmer = Swimmer()
    
    def quack(self):
        return 'Quack!'
    
    def start_fly(self):
        return self.flyer.fly()
    
    def start_swim(self):
        return self.swimmer.swim()
    
    def do_something(self):
        return self.swimmer.do_something()

donald = Duck()
print(donald.start_fly())
print(donald.start_swim())
print(donald.quack())
print(donald.do_something())