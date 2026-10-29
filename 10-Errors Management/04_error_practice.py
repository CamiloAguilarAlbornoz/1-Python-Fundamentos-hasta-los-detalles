class InvalidAgeError(Exception):
    
    def __init__(self, age, message = 'La edad debe ser mayor o igual a 18.'):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InvalidEmailError(Exception):
    
    def __init__(self, email, message = 'El correo electrónico debe contar con @ y . al final'):
        self.email = email
        self.message = message
        super().__init__(self.message)

def register_user(name, age, email):
    if age < 18:
        raise InvalidAgeError(age)
    if '@' not in email or '.' not in email.split('@')[-1]:
        raise InvalidEmailError(email)
    return f'Usuario {name} registrado con la edad {age} y el correo electrónico {email}'

try:
    print(register_user('Camilo', 29, 'camiloaaguilara@gmail.com'))
except InvalidAgeError as e:
    print(f'Error: {e}')
except InvalidEmailError as e:
    print(f'Error {e}')