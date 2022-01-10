

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
        self.caracteristicas = ""
        self.caractList = []
    
    def incluirCaracteristicas(self, caracts):
        self.caracteristicas = caracts

    def __str__(self): #SOBREESCRIBE print string
        return f'{self.marca} {self.modelo} {self.color} {self.caractList}'

    def __repr__(self): #SOBREESCRIBE string en LISTA , OBJETO, DICCIONARIO...
        return self.__str__()
    
    def export(self):
        mychars = ""
        if len(self.caracteristicas)>0:
            for caractr in self.caracteristicas:
                mychars+=(f';{caractr}')

        return f'{self.marca};{self.modelo};{self.color}{mychars}'

    def getCoche(self):
        return f"'marca': '{self.marca}', 'modelo': '{self.modelo}', 'color': '{self.color}'"
        # return dict(marca=f'{self.marca}', modelo=f'{self.modelo}', color=f'{self.color}')