DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def all_python_devs():
	""" 
	return all python developer 
	example
		['Facundo', 'Karo', 'Pablo', 'Lorena']

	"""
	print('all python devs', end='\n')
	print(' ', end='\n')
	all_python_devs =[worker['name'] for worker in DATA if worker['language']=='python']
	print(all_python_devs)

def all_platzi_workers():
	""" 
	return all platzi workers 
	example
		[
			{
				'name': 'Facundo', 
				'age': 72, 
				'organization': 'Platzi', 
				'position': 'Technical Coach', 
				'language': 'python', 
				'old': True 
			}
		]
		
	"""
	all_platzi_workers = [worker['name'] for worker in DATA if worker['organization']=='Platzi']
	print('all_platzi_workers', end='\n')
	print(' ', end='\n')
	print(all_platzi_workers)

def all_older():
	""" 
	return all platzi workers 
	example
		[
			{
				'name': 'Facundo', 
				'age': 72, 
				'organization': 'Platzi', 
				'position': 'Technical Coach', 
				'language': 'python', 
				'old': True 
			}
		]
		
	"""
	print('all older', end='\n')
	print(' ', end='\n')
	all_older = list(filter(lambda worker: worker['age'] > 18,DATA))
	print(all_older)
	return all_older

def all_adult():
	print('all older', end='\n')
	print(' ', end='\n')
	all_adult = list(map(lambda worker:(worker['name'],worker['age']), all_older()))
	print(all_adult)

def all_people():
	print('all people', end='\n')
	print(' ', end='\n')
	all_people = list(map(lambda worker:{ **worker, **{'old':worker['age']>40}},DATA))
	print(all_people)
	for x in all_people:
		print(x['age'],x['old'])

def run(func):
	func()
	

if __name__ == '__main__':
	for func in [all_python_devs, all_platzi_workers, all_older, all_adult, all_people]:
		run(func)

