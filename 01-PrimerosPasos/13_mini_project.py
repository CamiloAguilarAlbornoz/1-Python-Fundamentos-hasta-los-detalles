'''
Recibir de forma dinámica el nombre, el año de nacimiento, el correo y una contraseña

Imprimier los datos ingresados

Nombre: Camilo
Email: blablabla@
Tendrás en el 2050: n años
Tu contraseña es: ************* (la cantidad variarar dependiendo de la cantidad de caracteres)
'''

name = input('Ingresa tu nombre: ')
year_date = input('Ingresa tu año de nacimiento: ')
year_date = int(year_date)
email = input('Ingresa tu correo electrónico: ')
password = input('Ingresa tu contraseña: ')
password = '*' * len(password) # Coloca la cantidad de * que indique el metodo len()

answer = f'''
Nombre: {name}
Email: {email}
Tendras en el 2050: {2050 - year_date}
Tu contraseña es: {password}
'''
print(answer)