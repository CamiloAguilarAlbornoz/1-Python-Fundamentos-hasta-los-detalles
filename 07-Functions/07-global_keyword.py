tax = 16

def change_global():
    global tax # Con global se indica que la variable que se va a modificar es la global y no una local de la función
    tax = 18
    return tax

print(change_global())
print(tax)