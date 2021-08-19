def main():

	def palidromo(string):
		try:
			if len(string)==0:
				return valueError('no se puede ingresar cadenas vacias')
			return  string==string[::-1]
		except Exception as e:
			print(e)
			return False
		

	x = input('Ingrese un numero: ')
	try:
		print(palidromo(x))
	except Exception as e:
		print('solo se pueden ingresar string')
	finally:
		#se usa para cerrar una conexion, archivo, o liberar recursos
		#f.close()

		print('se ejecuto el codigo')
		

if __name__ == '__main__':
	main()