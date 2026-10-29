# Union => Crea un set con los elementos de los dos sets
set_one = {1, 2, 3, 4, 5}
set_two = {4, 5, 6, 7, 8}
union_set = set_one.union(set_two)
print(union_set)

# Intersection => Crea un set con los elementos en común de los dos sets
intersection_set = set_one.intersection(set_two)
print(intersection_set)

# Difference => si se invoca set_one.difference(set_two) retorna los elementos de set_one, no toma en cuenta los que tengan en comun ambos sets
difference_set = set_one.difference(set_two)
print(difference_set)