

def sumar(valor, valor2, *numeros):
    resultado = valor + valor2
    for numero in numeros:
            resultado += numero
    return resultado

print(sumar(4,4))


def factorial(numero):
    resultado = 1
    while numero > 0:
        resultado *=numero
        numero-=1
    return resultado

print(factorial(4))

def factorial_recursivo(num):
    if num<0:
        raise Exception('Numero en negatico no permitido')
    if num==0:
        return 1
    
    return num * factorial_recursivo(num-1)


print(factorial_recursivo(4))