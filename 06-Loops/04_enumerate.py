# enumerate empaqueta lo que se quiere iterar y permite acceder a datos como el index
for index, char in enumerate('Programación'):
    print(index, char)

print()

for index, number in enumerate([100, 120, 342, 5454]):
    print(index, number)

print()

for index, number in enumerate(list(range(100))):
    print(index, number)
    if number == 30:
        print('Aqui estoy')