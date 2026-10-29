class Person:
    
    '''
    Esta es la forma en que se define un constructor
    
    self ==> Se refiere al objeto o clase como tal
    '''
    def __init__(self, name, age):
        if age > 18:
            self.name = name
            self.age = age

person_one = Person('Silvana', 28)
print(person_one.name, person_one.age)

person_two = Person('Mayerly', 28)
print(person_two.name, person_two.age)

person_three = Person('Dayana', 29)
print(person_three.name, person_three.age)

person_four = Person('Carolina', 27)
print(person_four.name, person_four.age)

person_three = Person('Angela', 17)
print(person_three.name, person_three.age)