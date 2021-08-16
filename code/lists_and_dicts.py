def main():
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
	for key,values in superdict.items():
		print(key, values)
if __name__ == '__main__':
	main()