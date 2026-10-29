class CoffeMaker:
    
    def __boil_water(self):
        pass
    
    def __mix(self):
        pass
    
    def make_coffe(self):
        self.__boil_water()
        self.__mix()
        return True

coffe_maker = CoffeMaker()
coffe_was_made = coffe_maker.make_coffe()

if coffe_was_made:
    print('PIP PIP')
    print('Tu café está listo')