#******Tuples******#

meses = ('Enero', 'Febrero' , 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

# for n, meses in enumerate(meses):
#     print(n+1,meses)


#Modificar tupla (tuple)

# lista_meses = list(meses)
# lista_meses[0] = 'notEnero'
# meses = tuple(lista_meses)
# print(meses)
# print(lista_meses)


#******Sets******#

# meses = {'Enero', 'Febrero' , 'Marzo'}
# print(meses)
# meses.add('Febrero')
# print(meses)
# meses.remove('Febrero')
# print(meses)

# item = meses.pop()
# print(meses, item)

#******Objetos o Jsons?******#

tesla = {
    'marca': 'Tesla',
    'modelo': 'Roadster 2020',
    'color': 'rojo',
    'puertas': 4,
    'ruedas': 4
}

ford = {
    'marca': 'Ford',
    'modelo': 'Mustand',
    'color': 'Negro mate',
    'puertas': 4,
    'ruedas': 4
}


#print(coche['marca']) print(coche['modelo'])

for clave in tesla.values(): # [values() para valores - keys() para claves]
    # print(clave, tesla[clave]) #sin valores values() ni keys()
    print(clave)

tesla['color'] = 'rosa'
print(tesla)


#******DICCIONARIOS******

#Array de coches
coches = [tesla, ford]

print(coches[0]['color'])

for coche in coches:
    if coche['marca'] == 'Tesla':
        coche['color'] = 'rojo'

print(coches)

#Diccionario:
coches = {
    'tesla':{
        'marca': 'Tesla',
        'modelo': 'Roadster 2020',
        'color': 'Negro mate',
        'puertas': 4,
        'ruedas': 4  
    },
    'ford':{
        'marca': 'Ford',
        'modelo': 'Mustand',
        'color': 'Negro mate',
        'puertas': 4,
        'ruedas': 4  
    }
}

coches['tesla']['color'] = 'Blanco'


