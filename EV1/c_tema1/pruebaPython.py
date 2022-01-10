def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(500)


#VER TIPO DE DATO
print(type("ad"))

#LISTA
[10, 20, 30, 55]
[10, "hola", 30.1, True, "adios"]
[]

#TUPLE (Conjunto ordenado e inmutable de elementos)
(10, 20, 30, 55)
(10, "hola", 30.1, True, "adios")
()

#DICTORIONIES
{
    "name":"Ruben",
    "lastname":"Zuniga",
    "nick":"Cramike",
    "edad":19
}

None #No esta definido aun por un tipo de dato.

#VARIABLES

name="Ruben Zuniga"
edad=19

def saludos(n,e):
    print("Saludos " + n)
    print("  -edad: ".format(edad))

saludos(name, edad)

#STRINGS

print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.capitalize())
print(name.replace("Ruben", "Ruben cramike")) #cambia @1 por @2
print(name.count("n"))
print(name.startswith("Ru"))
print(name.split()) #['Ruben', 'Zuniga']
print(name.index("e"))
print(name[3])

print("My age is {0}".format(edad)) #print("My age is {}".format(edad))
