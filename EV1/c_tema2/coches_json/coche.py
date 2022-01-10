class Coche:

    def __init__(self, marca, modelo, color, extras = []):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.extras = extras
    
    def export(self):
        return f'{self.marca};{self.modelo};{self.color}'

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.color} -> {self.extras}'

    def __repr__(self):
        return self.__str__()