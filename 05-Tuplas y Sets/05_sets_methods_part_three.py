set_one = {1, 2, 3, 4}
set_two = {3, 4, 5, 6}

# symmetric_difference => Retorna los elementos de ambos sets que no coincidan
symmecric_difference = set_one.symmetric_difference(set_two)
print(symmecric_difference)

# issubset => Evalua si el set_one es un subconjunto del set_two
set_three = {1, 2}
set_four = {1, 2, 3, 4}
print(set_three.issubset(set_four))

#issuperset => Dice si es un super conjunto, depende de que el primer set tenga todos los elementos del segundo
set_five = {1, 2, 3, 4}
set_six = {1, 2}
print(set_five.issuperset(set_six))