# import calculadora
# from calculadora import sumar, factorial

# print(calculadora.sumar(3,3))
# print(sumar(3,6))
# print(factorial(3))

# if __name__ == '__main__':
#     print(sumar(10,20))

import enum
from vehiculos import Coche

coche1 = Coche('Tesla', 'Roadster 2020', 'Rojo')
coche2 = Coche('Ford', 'Mustand', 'Gris Oscuro')

# print(coche1)
# print(coches)


coches = [coche1, coche2]

# coches_dict = {coche1.marca: coche1, coche2.marca: coche2}
coches_dict={}

for coche in coches:
    coches_dict[coche.marca] = coche

print(coches_dict)

try:
    print(coches_dict['Tesla'])
except KeyError as e: #o except Exception:
    print(str(e))
    pass



# coches[0].mover(20)

# print(f'{coches[0].modelo} {coches[0].color}')

# for coche in coches:
#     if coche.marca == 'Tesla':
#         coche.mover(69)
#         print('Total recorrido:', coche.odometro)
#         break
#     # print(coche.marca,coche.modelo)
    

