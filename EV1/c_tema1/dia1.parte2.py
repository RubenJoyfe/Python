lista = ['cero','uno','dos']
nums = [21,31,51,12,5,1,512,5,1,51,5,21,41,34,1,4]

print(len(lista))
print(nums[6:9]) #coger rango de elementos de la lista

for item in lista:
    print(item, end= '' if item == lista[-1] else ' - ')

print( )
print(7 // 2) #Devuelve la parte entera de un número

mitad = (len(nums)-1) //2

if len(nums) %2 == 0:
    nums.insert(mitad, '69')
print(nums)

nums[mitad+1]= '6969'
print(nums)

for index, item in enumerate(nums):
    print(f'{index} - {item}')


