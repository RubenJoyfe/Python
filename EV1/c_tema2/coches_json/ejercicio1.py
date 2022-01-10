import os, json
from coche import Coche

path_base = os.path.dirname(os.path.abspath(__file__))

coches = []

with open(f'{path_base}/coches.txt', 'r',  encoding='UTF-8') as archivo:
    data = archivo.read()

coches_dict = json.loads(data)

for coche in coches_dict:
    if 'extras' in coche and 'personas' in coche:
        print(coche)

# print(coches_dict)
exit(0)
# OPCION 1
while True:
    coche = {}
    coche['marca'] = input('Marca: ')
    coche['modelo'] = input('Modelo: ')
    coche['color'] = input('Color: ')
    extras = input('Extras (separadas por coma): ')
    coche['extras'] = extras.split(',')
    personas = input('Conductores (separados por coma): ')
    coche['personas'] = personas.split(',')
    coches_dict.append(coche)

    with open(f'{path_base}/coches.txt', 'w',  encoding='UTF-8') as archivo:
        archivo.write(json.dumps(coches_dict, indent=4))

    continuar = input('Continuar? ')
    if continuar.lower() not in ['y', 'yes', 'si', 's']:
        break

# OPCION 2
while False:
    coche = Coche(None, None, None)
    coche.marca = input('Marca: ')
    coche.modelo = input('Modelo: ')
    coche.color = input('Color: ')

    with open(f'{path_base}/coches.txt', 'a',  encoding='UTF-8') as archivo:
        archivo.write(f"{coche.export()}\n")

    continuar = input('Continuar? ')
    if continuar.lower() not in ['y', 'yes', 'si', 's']:
        break