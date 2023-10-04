<div align="center">

# 🦾 **Programa 2** 🔮



# **Búsquedas Binarias**


</div>


<div align="center">

[![](https://media.giphy.com/media/oWQzTz2A4fp1m/giphy-downsized-large.gif)](https://www.youtube.com/watch?v=SBjQ9tuuTJQ)

</div>


---

## **Uso**

Para correr el programa que realiza **Busqueda Binaria**
- Compilar desde `src/`:

Linux  : 

```Haskell
\src> python3 busquedaBinaria.py <nombreArchivo.txt> <numero entero a buscar>
```

Windows:  

```Python
\src> python busquedaBinaria.py <nombreArchivo.txt> <numero entero a buscar>
```

Para el funcionamiento del programa, se debe proporcionar un archivo **.txt** (el cual debe estar en src)  con una sucesion ordenada de numeros enteros separados por comas y el numero entero a buscar.

----

Para correr el programa que realiza **Busqueda Binaria de un Indice Especial**
- Compilar desde `src/`:

Linux  : 

```Haskell
\src> python3 programa02.py <nombreArchivo.txt>
```

Windows:  

```Python
\src> python programa02.py <nombreArchivo.txt>
```

Para el funcionamiento del programa, se debe proporcionar un archivo **.txt** (el cual debe estar en src)  con una sucesion ordenada de numeros enteros separados por comas.


<div align="center">

---
# **Busqueda Binaria**

</div>

La razón de ser de los algoritmos de búsqueda es que, precisamente, necesitamos saber si se encuentra un elemento (y donde se encuentra), en algún determinado espacio de búsqueda, de esta forma nacen múltiples algoritmos de búsqueda que satisfacen diferentes tipos de problemas con diferentes espacios de búsqueda, es aquí donde entra Búsqueda Binaria.

Este algoritmo fue inventado alrededor de 1960, el algoritmo consiste en buscar la mitad del espacio de búsqueda y con esto dividir el espacio de búsqueda en 2, para que de esta forma podamos irnos a la mitad en la que debería estar el elemento que estamos buscando (cabe resaltar que el algoritmo considera en su entrada una lista ordenada, los resultados con listas que no están ordenadas pueden ser volátiles-erróneos), el algoritmo repite este proceso hasta que encuentre (o no) el elemento que estemos buscando.

Ejemplo de uso con el programa:

```Python
\src> python busquedaBinaria.py listaNumeros.txt 21
Elemento buscado: 21
Espacio de busqueda inicial: [-2, -1, 0, 2, 3, 5, 6, 9, 10, 13, 21]
Iteracion 1: Espacio de busqueda: [6, 9, 10, 13, 21]
Iteracion 2: Espacio de busqueda: [13, 21]
Iteracion 3: Espacio de busqueda: [21]
Elemento encontrado en el indice 11.
Numero total de iteraciones: 4
El elemento 21 se encuentra en el indice 11.
```

---

<div align="center">
  
# **Busqueda Binaria de un Índice Especial**

</div>

Con este tipo de variante de Búsqueda Binaria, ya no vamos a recibir una lista y un elemento el cual buscar, ahora  solo vamos a recibir una lista y a raíz de esta, queremos satisfacer si; 
Dada una secuencia ordenada de enteros distintos: $a_1,  a_2, ... , a_n$
determinar si existe un índice $i$ tal que $a_i = i$
Es decir, si por ejemplo le pasamos la lista $L$ (previamente ordenada)     
$L = \{-5,-4,-2,0,1,3,5,7,8,9,11,13,14,15,16\}$

notaremos que si existe un índice $a_i = i$ ya que el $11$ lo cumple. 

$indices :[ 1,  2,  3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]$

$elemL :\{-5, -4, -2, 0, 1, 3, 5, 7, 8,  9, 11, 13, 14, 15, 16\}$

Ejemplo de uso con el programa:

```Python
\src> python programa02.py listota.txt
Espacio de busqueda: [-5, -4, -2, 0, 1, 3, 5, 7, 8, 9, 11, 13, 14, 15, 16]
Espacio de busqueda: [8, 9, 11, 13, 14, 15, 16]
Espacio de busqueda: [8, 9, 11, 13]
Espacio de busqueda: [11, 13]
Espacio de busqueda: [11]
Numero total de iteraciones: 5
Indice especial encontrado en el indice 11: 11
```
