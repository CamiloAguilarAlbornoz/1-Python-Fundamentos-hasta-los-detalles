# For: Ayuda para iterables, cuando sabemos cuando terminara
# While: Cuando no sabemos cuando terminará y necesitamos una condición

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
print()
item = 1
while item <= len(my_list):
    print(item)
    item += 1