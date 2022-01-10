
import os

# print('\n',os.getcwd(),'\n')
path_base = os.path.dirname(os.path.abspath(__file__))

archivo = open('./c_tema2/datos.txt', 'r')

print(archivo.read())

archivo.close()

#ALTERNATIVA (se cierra solo)
#
# with open('./c_tema2/datos.txt', 'r') as archivo:
#     texto = archivo.read()
# print(texto)

# READ WRITE APPEND: with open('./c_tema2/datos.txt', 'r') as archivo: with open('./c_tema2/datos.txt', 'w') as archivo: with open('./c_tema2/datos.txt', 'a') as archivo:

# with open(f'{path_base}/datos.txt', 'a', encoding='UTF-8') as archivo:
#     archivo.write('\n¿Qué tal?')

#notas

#read(6) leer letras
#readlines() leer lineas
#readline() leer linea

with open(f'{path_base}/datos.txt', 'r', encoding='UTF-8') as archivo:
    line = archivo.readline()
    while line:
        line = archivo.readline()
        print(line)



#HACER SCRIPT
#Introducir coches (marca, modelo, coche)<-con bucle
#Una vez introducido lo metes todo en un archivo
#¿Quieres añadir otro coche? Si/No
#
#