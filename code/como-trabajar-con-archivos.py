def write():
	names =['edwight','david','carlos']
	with open('./files/names.txt','a', encoding='utf-8') as f:
		for name in names:
			f.write(name)
			f.write('\n')

def read():
	numbers=[]
	with open('./files/numbers.txt','r',encoding='utf-8') as f:
		for line in f:
			print(line)
			#numbers.append(int(line))
	print(numbers)

def main():
	read()
	write()

if __name__ == '__main__':
	main()