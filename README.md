# Python Intermedio

## Clase 5 y 7: Indexado y manejo de archivos CSV

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
  
