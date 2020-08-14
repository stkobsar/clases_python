

""""
Base class! --> General
"""
class Coche():

    def __init__(self, puertas):
        self.puertas = puertas

    def get_puertas(self):
        print(self.puertas)



"""
Children class! --> Especifico
"""
class Mercedes(Coche):

    def __init__(self, automata, puertas):
        super().__init__(puertas)
        self.automata = automata

    def get_automata(self):
        """
        Print if is automata
        :return:
        """
        print(self.automata)

class Porsche(Coche):

    def __init__(self, fly, puertas):
        super().__init__(puertas)
        self.fly = fly

    def get_fly(self):
        print(self.fly)


if __name__ == "__main__":
    """
    1) Objeto con una logica (coche) dentro tengas ciertos adjetivos (atributos)
    2) Herencia  --> Porche, mercedes (comunes) --> Coche, (especificas) --> Merced, Porche 
    """
    coche_mercedes = Mercedes(True, 4)
    coche_mercedes.get_automata()
    coche_mercedes.get_puertas()


    coche_porsche = Porsche(False, 2)
    coche_porsche.get_fly()

