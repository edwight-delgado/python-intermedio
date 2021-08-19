# Python Intermedio

###  Profesor Facundo García Martoni 
### plataforma [Platzi](https://platzi.com/clases/2255-python-intermedio/)

### Creando un ambiente virtual con VENV
Creación de ambiente Virtual:

    python3 -m venv nombre_venv

-   Usualmente el nombre del ambiente virtual es venv. 
-   el flag - m indica que estamos llamando un modulo interno 

Activación del ambiente virtual:

-   Windows:

`.\venv\Scripts\activate`

-   Unix o MacOS:

`source venv/bin/activate`

Desactivar el ambiente virtual:

`deactivate`

Crear un alias en linux/mac:

`alias nombre-alias="comando"`

Ejemplo

`alias avenv=“source venv/bin/activate”``

ahora para activar

    avenv
y para desactivar

    deactivate


### Instalación de Dependencias Con Pip

**Pip (package installer for python)**  Nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, ademas se puede definir una versión especifica del paquete.  


-   `pip install <paquete>`  instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique
    
-   `pip freeze`  muestra todos los paquetes instalados en tu ambiente virtual
    
Si quisiéramos que alguien mas pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:

```
pip freeze > requirements.txt
```
El resultado de  `pip freeze`  se escribe en  `requirements.txt`  (puedes usar otro nombre pero el mostrado es una buena practica)  

para instalar paquetes desde un archivo como  `requirements.txt`  ejecutamos:
```
pip install -r requirements.txt 
```
### List comprehensions

    squares = [i for i in range(1000) if i %39==0]
print(squares)

### Dict comprehensions
**Solucionando**  el  **problema propuesto**  con  **Dictionary comprehensions**.

```python
def run():
    dictionary = {i: i**3 for i in range(1, 101)}
    print(dictionary)


if __name__ == "__main__":
    run()
```

### Funciones anonimas lambda
![enter image description here](https://i1.faceprep.in/Companies-1/python-lambda-functions-new.png)

Ejemplos:

🐍 Las  **funciones**  **anónimas**  nos permiten tener funciones sin  **nombre (identificador)**. En  **Python**  son conocidas como funciones  **lambda**.

```python
palindrome = lambda string: string == string[::-1]
print(palindrome('ana'))#ala
```
otro ejemplo:

    lambda x: x.replace(" ", "").lower() == x[::-1].replace(" ", "").lower()

un  ejemplo más:

    sqr = lambda (x,y):x**y
    print(sqr(2,5))

### High order functions: filter, map y reduce
  La diferencia entre  **filter y map**:

-   _filter_  devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.
-   _Map_  funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.

Cómo funciona  **reduce**:

-   _Reduce_  toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.
![enter image description here](https://dz2cdn1.dzone.com/storage/temp/11727498-download.png)
Acá le dejo el código de la clase para poder practicar y entender:

```
from functools import reduce
def main():

    #Filter
    myList = [1,4,5,7,9,13,19,21]

    odd = list(filter(lambda x: x % 2 != 0, myList))
    print(odd)

    #Map
    myList2 = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, myList2))
    print(squares)

    myList3 = [2, 2, 2, 2, 2]
    
    allMultiplied = reduce(lambda a, b: a * b, myList3)
    print(allMultiplied)

if __name__ == '__main__':
    main()
```
### Proyecto filtrado de datos

### Los errores en el código
**Errores en el código**  
Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puesde ser debido a:

-   Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
-   Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)

**Lectura de un traceback**

-   La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
-   En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
-   La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
-   La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

**Elevar una excepción**

-   Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

Estos son los errrores y excepciones de la documentacion oficial de python

[https://docs.python.org/es/3/tutorial/errors.html](https://docs.python.org/es/3/tutorial/errors.html)

### Debugging
https://docs.python.org/es/3/library/pdb.html

### Manejo de excepciones
Algo que aparece casi al final de la lectura recomendada en el documentación de Python es que se puede agregar un “else” al try-except.

**TRY**: En el try se coloca código que esperamos que pueda lanzar algún error.  
**EXCEPT**: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.  
**ELSE**: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try  
**FINALLY**: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

![enter image description here](https://static.platzi.com/media/user_upload/python-a0d427c5-4e5b-49cd-8e69-3e3b118f37ce.jpg)

### Poniendo a prueba el manejo de excepciones

### Assert statements
**Assert statements**

-   Es una manera poco usual de manejar los errores en python
-   Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo  `AssertionError`  y nos muestra un mensaje.
-   Su sintaxis es:

```
assert <condicion>, <"mensaje">
<código>
```

ejemplo

    def divisor(num):
	#assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
    divisors = [i for i in range(1,num+1) if num%i == 0]
    return divisors

    def run():
        num = input('Enter a number: ')
        assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
        print(divisor(int(num)))
        print('Finish')
    
    
    if __name__ == '__main__':
        run()

### Como trabajar con archivos
**Modos de Apertura**

-   **r**  -> Solo lectura
-   **r+**  -> Lectura y escritura
-   **w**  -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
-   **w+**  -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
-   **a**  -> Añadido (agregar contenido). Crea el archivo si éste no existe
-   **a+**  -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

Para abrir un archivo seguimos las siguiente estructura

```python
with open(<ruta>, <modo_apertura>) as <nombre>

```

`with`  Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

`open(ruta,modo_apertura)`: es una función que necesita de dos parámetros

-   `ruta`: es donde se encuentra nuestro archivo en nuestro equipo
    
-   `modo_de_apertura`: como vamos a abrir el archivo, los modificadores son:  
    r → modo de lectura  
    w → modo de escritura (sobreescribe el archivo)  
    a → modo append (añade información al final del archivo)
    

`as <nombre>`  nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer

Ejemplo:

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



  
