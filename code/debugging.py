import pdb; pdb.set_trace() 

def divisor(num)->int:
	divisor=[]
	for i in range(1, num+1):
		if num%i == 0:
			divisor.append(i)
	return divisor

def main():
	num=int(input('Ingresa un numero: '))
	print(divisor(num))
	print('termino el programa')
if __name__ == '__main__':
	main()