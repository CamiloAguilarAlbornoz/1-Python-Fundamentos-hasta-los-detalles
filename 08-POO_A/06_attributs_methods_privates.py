class Person:
    
    '''
    Esta es la forma en que se define un constructor
    
    self ==> Se refiere al objeto o clase como tal
    '''
    def __init__(self, name, age):
        self.name = name # Atributos de instancia
        self.__password = '1234' # Si tiene __, es decir doble guion bajo, indica que el atributo es privado, por el mangling el atributo es inaxesible
        self.age = age
    
    def __generate_password(self):
        return f'$${self.name}{self.age}'

person_one = Person('Camilo', 29)
print(person_one.name)
person_one._Person__generate_password()
print(person_one._Person__password) # El acceso a un atributo privado es con _Classatributo, ejemplo _Person__password