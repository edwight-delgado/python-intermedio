#hay que importar reduce para poder usarlo 
from functools import reduce
def saludo(func):
	func()

def hola():
	print('hola')

def adios():
	print('adios')

saludo(hola)
saludo(adios)

#usando filter
#filtrar los numeros impares de una lista de numeros
mylist = [i for i in range(100)]

odd=list(filter(lambda x: x%2!=0, mylist))

print(odd)

#usando map
#usar map para aplicar transformar una lista de numeros 
sqr = list(map(lambda x:(x,x**2),mylist))
print(sqr)

#usando map
#usar map para aplicar transformar una lista de numeros 
mylist3 = [2, 2, 2, 2, 2]
allMultiplied  = reduce(lambda a, b: a*b, mylist3)
print(allMultiplied)