for item in 'Python':
    print(item)

fruits = ['manzana', 'platano', 'sandia']
for fruit in fruits:
    print(fruit)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
final_message = ''
for mult in my_list:
    sum += mult
    final_message += f'\nTabla del {mult}\n\n'
    for multplicator in my_list:
        final_message += f'{mult} x {multplicator} = {mult * multplicator}\n'
final_message += f'\n\nSuma = {sum}'
print(final_message)