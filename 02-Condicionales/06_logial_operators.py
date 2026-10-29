## Evaluar condiciones
#
## ================ and que en otros es &&
#'''
#Evalua si dos condiciones o más son verdaderas
#si una no se cumple, será falso
#'''
#print(True and True) # true
#print(True and False) # false
#print(False and True) # false
#print(False and False) # false
#
## ================ or que en otros es ||
#'''
#Evalua que al menos un valor sea true
#'''
#print(True or True) # true
#print(True or False) # true
#print(False or True) # true
#print(False or False) # false
#
## ================ not que en otros es !
#'''
#Se ecarag de una negación
#'''
#print(not True) # false
#print(not False) # true

###################### Prueba and
age = 25
licenced = True

if age >= 18 and licenced:
    print('Puedes conducir')

###################### Prueba or
is_estudent = False
membership = True

if is_estudent or membership:
    print('Puedes obtener el descuento especial')

###################### Prueba not
is_admin = True
if not is_admin:
    print('Acceso denegado')