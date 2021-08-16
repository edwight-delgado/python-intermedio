def main():
	""" lists and dicts """
	my_list=[1,'verdad',True,4.5]
	my_dict={'firstname':'edwight','lastname':'delgado'}

	superlist=[
		{'firstname':'edgar','lastname':'barreto'},
		{'firstname':'ramon','lastname':'castillo'},
		{'firstname':'juan','lastname':'medina'}
	]
	superdict={
		'natural_list':[1,2,3,4],
		'integer_nums':[-5,-4,-3,-2],
		'floting_nums':[2.3,5.6,-2.8],
	}
	print('super dicts')
	for key,values in superdict.items():
		print(key, values)

	print('super list 1')
	for lista in superlist:
		print('firstname: ',lista['firstname'],', lastname: ',lista['lastname'])

	print('super list 2')
	for lista in superlist:
		for key, value in lista.items():
			print(f'{key},{value}')

if __name__ == '__main__':
	main()