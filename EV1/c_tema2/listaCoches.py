import os
from coches import Coche

path_base = os.path.dirname(os.path.abspath(__file__))
coches_list=[]

def introducirCoche():
    marca = input("Introduzca marca del coche: ")
    modelo = input(f"Introduzca modelo del coche {marca}: ")
    color = input("Introduzca color del coche: ")
    caract = introducirCaracteristicas()
    car = Coche(marca, modelo, color)
    if caract != 0:
        car.incluirCaracteristicas(caract)
    writeFile(car)

def introducirCaracteristicas():
    intr = None
    caracteristicas=[]
    while intr != 'n':
        intr = input('Desea introducir características? (y/n)')
        if intr == 'n':
            if len(caracteristicas) == 0:
                return 0
            else:
                return caracteristicas
        else:
            caracteristica = input('Introduzca característica: ')
            caracteristicas.append(caracteristica)

def pedirCoches():
    seguir = 1
    while seguir != 0:
        introducirCoche()
        seguir = preguntarSeguir()

def preguntarSeguir():
    respuesta = ''
    while respuesta != 'y' and respuesta != 'n':
        respuesta = input('Desea seguir introduciendo coches? (y/n)')
        if respuesta == 'n':
            return 0

def writeFile(coche):
    with open(f'{path_base}/coches.txt', 'a', encoding='UTF-8') as archivo:
        archivo.write(f'{coche.export()}\n')

def leerCoches():
    with open(f'{path_base}/coches.txt', 'r', encoding='UTF-8') as archivo:
        data = archivo.read()
        data = data.split('\n')
        for coche_str in data:
            values = coche_str.split(';')
            if len(values) > 2:
                mycar = Coche(values[0], values[1], values[2])
                values = values[3:]
                for value in values:
                    mycar.caractList.append(value)
                coches_list.append(mycar)


# pedirCoches()
leerCoches()
print(coches_list)




#otra forma
# import os
# from coches import Coche

# path_base = os.path.dirname(os.path.abspath(__file__))
# coches_list=[]

# def introducirCoche():
#     coche = {}
#     coche['marca'] = input("Introduzca marca del coche: ")
#     coche['modelo'] = input(f"Introduzca modelo del coche {coche['marca']}: ")
#     coche['color'] = input("Introduzca color del coche: ")
#     car = Coche(coche['marca'], coche['modelo'], coche['color'])
#     writeFile(coche['marca'],coche['modelo'],coche['color'], car)


# def pedirCoches():
#     seguir = 1
#     while seguir != 0:
#         print(seguir)
#         introducirCoche()
#         seguir = preguntarSeguir()


# def preguntarSeguir():
#     respuesta = ''
#     while respuesta != 'y' and respuesta != 'n':
#         respuesta = input('Desea seguir introducioendo coches? (y/n)')
#         if respuesta == 'n':
#             return 0

# def writeFile(marca,modelo,color, coche):
#     print(coche.getCoche())
#     with open(f'{path_base}/coches.txt', 'a', encoding='UTF-8') as archivo:
#         archivo.write(f"{coche['marca']} {coche['modelo']} {coche['color']}\n")

# def leerCoches():
#     with open(f'{path_base}/coches.txt', 'r', encoding='UTF-8') as archivo:
#         line = archivo.readline()
#         while line:
#             print(line)
#             coches_list.append(line[:-1])
#             line = archivo.readline()

# pedirCoches()
# leerCoches()
# print(coches_list)


#{'marca': 'Tesla', 'modelo': 'X', 'color': 'Rojo'}
#{'marca': 'Fiat', 'modelo': 'Multipla', 'color': 'Verde catcus'}






#ORIGINAL

# import os
# from coches import Coche

# path_base = os.path.dirname(os.path.abspath(__file__))
# coches_list=[]

# def introducirCoche():
#     marca = input("Introduzca marca del coche: ")
#     modelo = input(f"Introduzca modelo del coche {marca}: ")
#     color = input("Introduzca color del coche: ")
#     car = Coche(marca, modelo, color)
#     writeFile(car)


# def pedirCoches():
#     seguir = 1
#     while seguir != 0:
#         print(seguir)
#         introducirCoche()
#         seguir = preguntarSeguir()


# def preguntarSeguir():
#     respuesta = ''
#     while respuesta != 'y' and respuesta != 'n':
#         respuesta = input('Desea seguir introducioendo coches? (y/n)')
#         if respuesta == 'n':
#             return 0

# def writeFile(coche):
#     print(coche.getCoche())
#     with open(f'{path_base}/coches.txt', 'a', encoding='UTF-8') as archivo:
#         archivo.write('{' + coche.getCoche() + '}\n')

# def leerCoches():
#     with open(f'{path_base}/coches.txt', 'r', encoding='UTF-8') as archivo:
#         line = archivo.readline()
#         while line:
#             print(line)
#             coches_list.append(line[:-1])
#             line = archivo.readline()

# # pedirCoches()
# leerCoches()
# print(coches_list)
