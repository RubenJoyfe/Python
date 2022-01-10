lista = ['cero','uno','dos']

#encontrar elemento en la lista

buscNum = input('Escribe un numero: ')

if buscNum in lista:
    print('Este elemento está en la lista')
else:
    print('Este elemento NO ESTÁ en la lista')

lista.append('ultimo')
print(lista)
lista.remove('ultimo') #remove o pop(pop solo para numeros)
print(lista)

while len(lista) < 15:
    lista.append('uno')

print(lista)
print('Borrando unos de la lista...')

while 'uno' in lista:
    lista.remove('uno')

print('unos borrados')
print(lista)

pregBorrList = input('Desea borrar lista? y/n: ')

if pregBorrList == 'y' or pregBorrList == 's':
    lista.clear()
    print(f'lista borrada: {lista}')
    