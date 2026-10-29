shopping_cart = ['Camisas', 'Tenis', 'Medias', 'Pantalones']
new_list = shopping_cart[1:4] # A esto se conoce como slicing o rebanar

new_list[0] = 'Zapatos'
new_list[1] = 'Collar'

print(new_list)
print(shopping_cart)

new_cart = shopping_cart[:] # Copia los elementos de la lista
new_cart[0] = 'Playeras'
print(f'La nueva lista tras copiarle shopping_cart {new_cart}')