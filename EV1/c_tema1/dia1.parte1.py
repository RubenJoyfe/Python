def pruebaEdad():
    if num<18 and (nom=="Ligma" and ape=="boals"):
        print("Menor SOs pUt0")
    else:
        print("pase susteh")


num=13
nom="Ligma"
ape='boals'

variable = "Hola "+nom+" "+ape+" "+str(num)

print(variable)

variable = f'Hola {nom} {ape}, tu edad es {num*2}'

print(variable)

pruebaEdad()

while num < 18:
    print(num)
    num+=1

pruebaEdad()

edad = input("Confirma tu edad aquí: ")

if edad!= num:
    print("La edad introducida es incorrecta, mentiroso")
else:
    print("que dios le bendiga")

print(f"El dato introducido es {edad}")


try:
    midato = input("Introduzca un numero")
    midato = int(midato)
    # midato = midato/0
    print("Gracias por hacerme caso")
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception:
    print("INUTIIIIL! Te he dicho que introduzcas un numero")
except :
    print("Something went wrong")