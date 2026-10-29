def outer():
    enclosing_variable = 'Enclosing Variable'
    
    def inner():
        nonlocal enclosing_variable # Indica que la variable a modificar es la que no es local pero que está en el método superior, o sea outer()
        enclosing_variable = 'Enclosing Modificado'
    inner()
    print(enclosing_variable)
outer()