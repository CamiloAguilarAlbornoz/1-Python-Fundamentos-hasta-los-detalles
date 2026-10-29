class Person:

    specie = 'Humano'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod # Indica que el método funciona no a nivel de clase sino a nivel de clase, de forma que si se invoca afectara a todas las instancias que se hagan con esta clase
    def change_spacies(cls, new_specie): # Se expresa con cls
        cls.specie = new_specie
    
    @staticmethod # Indica que el método es estático y es independiente de la instancia y de los atributos de clase
    def is_older(age):
        return age >= 18

person_one = Person('Camilo', 29)
print(person_one.specie)
Person.change_spacies('Cyborg') # Se invoca con el nombre de clase
print(person_one.specie)

person_two = Person('Carolina', 27)
print(person_two.specie)

print(Person.is_older(person_two.age))