from math import sqrt
def main():
	"""dict comprehensions"""
	dictm={}
	for x in range(1,100):
		dictm[x]=x**2

	print(dictm,end='\n')
	print('usando dict comprehensions')
	s= {x:x**2 for x in range(1,100) if x%2==0 }
	print(s)
	print('reto raiz cuadrada')
	sq ={i:sqrt(i) for i in range(1000)}
	print(sq)
if __name__ == '__main__':
	main()