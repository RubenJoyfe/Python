import os, json
from coche import Coche

path_base = os.path.dirname(os.path.abspath(__file__))

coches_dict = ()
coches = []

with open(f'{path_base}/coches.json', 'r',  encoding='UTF-8') as archivo:
    data = archivo.read()

coches_dict = json.loads(data)

# coches = [Coche(c['marca'], c['modelo'], c['color'], c['extras']) for c in coches_dict]  #lo mismo que el bucle de abajo

for c in coches_dict:
    print(c)
    # coches.append(Coche(c['marca'], c['modelo'], c['color'], c['extras']))
    coches.append(Coche(**c))

# coches = [Coche(**c) for c in coches_dict]

print(coches)
exit(0)

# for coche in coches_dict:
#     if 'extras' in coche and 'personas' in coche:
#         print(coche)

# print(coches_dict)

while True:
    coche = Coche(None, None, None)
    coche.marca = input('Marca: ')
    coche.modelo = input('Modelo: ')
    coche.color = input('Color: ')
    extras = input('Extras (separados por comas): ')
    coche.extras = extras.split(',')
    
    coches.append(coche)

    #Lo mismo que [c.__dict__ for c in coches]
    # lista = []
    # for c in coches:
    #     lista.append(c.__dict__)


    with open(f'{path_base}/coches.json', 'w',  encoding='UTF-8') as archivo:
        archivo.write(json.dumps([c.__dict__ for c in coches], indent=4))

    continuar = input('Continuar? ')
    if continuar.lower() not in ['y', 'yes', 'si', 's']:
        break