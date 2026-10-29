class Person:
    
    specie = 'Humano'
    
    '''
    Esta es la forma en que se define un constructor
    
    self ==> Se refiere al objeto o clase como tal
    '''
    def __init__(self, name, age):
        self.name = name # Atributos de instancia
        self.age = age
    
    def work(self):
        return f'{self.name} está trabajando muy duro'
    
    def eat(self, food):
        if food.lower() == 'tacos':
            return f'SUPERPOWERS'
        else:
            return 'Más energía'

person_one = Person('Silvana', 28)
print(person_one.name, person_one.age)

person_two = Person('Mayerly', 28)
print(person_two.name, person_two.age)

person_three = Person('Dayana', 29)
print(person_three.name, person_three.age, person_three.specie)
print(person_three.eat('TaCoS'))

person_four = Person('Carolina', 27)
print(person_four.name, person_four.age)
print(person_four.work())