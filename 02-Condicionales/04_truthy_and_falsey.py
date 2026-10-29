# Truthy son valores verdadeos
'''
Todo número diferente a 0 es Truthy
Un string que tenga contenido es Truthy
'''
print(bool(True))
print(bool(1))
print(bool(-1))
print(bool(1j))
print(bool('Hola'))
print(bool([1, 2, 3, 4])) # lista
print(bool((1, 2, 3, 4))) # tupla
print(bool({1, 2, 3, 4})) # set

# Falsey son valores falsos
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(''))
print(bool([])) # lista
print(bool(())) # tupla
print(bool({})) # set
print(bool(None)) # NADA