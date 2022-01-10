

class Vehiculo:
    
    #CONSTRUCTOR
    def __init__(self, marca):
        self.marca = marca
        self.odometro=0

        pass


    def mover(self, kilometros):
        print(f'Moviento el vehiculo {self.marca} {kilometros}km')
        self.odometro += kilometros
    


class Coche(Vehiculo):

    def __init__(self, marca, modelo, color):
        super().__init__(marca)
        self.modelo = modelo
        self.color = color
    
    def __str__(self): #SOBREESCRIBE print string
        return f'{self.marca} {self.modelo} ({self.color})'

    def __repr__(self): #SOBREESCRIBE string en LISTA , OBJETO, DICCIONARIO...
        return self.__str__()