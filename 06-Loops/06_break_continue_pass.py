# Pass
for item in [1, 2, 3, 4, 5]:
    pass

# Break
for item in [1, 2, 3, 4, 5]:
    if item == 4:
        break
    #dprint(item)

# Continue
number = 0
while(number < len([1, 2, 3, 4, 5])):
    number += 1
    continue # Ignora todo luego del continue
    print(number)