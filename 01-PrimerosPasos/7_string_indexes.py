name = 'Camilo'
print(name[0])
print(name[1])

# =========== Como obtener la ultima letra
print(f'La ultima letra {name[-1]}')

# =========== [Start:Stop]
print(name[0:4]) # Imprime Cami, toma en cuenta el inicio pero no el final, la 4 sería la l pero llega hasta el 3

# =========== [Start:Stop:stepover]
print(name[0:4:2]) # Indica cuantas letras se va a saltar para llegar desde el 0 hasta el anterior al 4, Imprime Cm

# Ejercicio
# Como poner mi nombre al revés
print(f'Mi nombre al revés es {name[::-1]}') # Poner :: obtiene toda la cadena, si como stepover se coloca -1, inicia desde la ultima, imprime olimaC