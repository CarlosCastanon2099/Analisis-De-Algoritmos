<div align="center">

#  📜 Programas 🗝️

##   Curso de Análisis de Algoritmos 2024-1
 
###  <em> Programas realizados durante el curso: </em>
</div>




```Julia
> -  Programa 01: Adoquinamiento
```


<div align="center">

![Adoquinamiento 16-16](./../Media/Adoquinamiento/4/adoquinamientoPasoaPaso.gif)

</div>



```Julia
> -  Programa 02: Búsquedas Binarias
```

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


\src> python programa02.py listota.txt
Espacio de busqueda: [-5, -4, -2, 0, 1, 3, 5, 7, 8, 9, 11, 13, 14, 15, 16]
Espacio de busqueda: [8, 9, 11, 13, 14, 15, 16]
Espacio de busqueda: [8, 9, 11, 13]
Espacio de busqueda: [11, 13]
Espacio de busqueda: [11]
Numero total de iteraciones: 5
Indice especial encontrado en el indice 11: 11
```





```Julia
> -  Programa 03: Ordenamientos
```

<div align="center">

![Selection](./../Media/Selection-Vel-75.gif)

</div>


```Julia
> -  Programa 04: Bosque Generador de Peso Mínimo
```

```Julia
\src> python Programa04.py prueba.txt
Grafica Original:
(Vertice1, Vertice2, Peso)

[(0, 1, 1), (7, 8, 1), (8, 6, 2), (1, 3, 3), (2, 1, 3), (4, 0, 3), (5, 6, 4), (3, 2, 5), (6, 7, 5)]

Bosque de Arboles de Peso Minimo de cada componente conexa:
Aristas del árbol de peso mínimo:
(0, 1, 1)
(1, 3, 3)
(2, 1, 3)
(4, 0, 3)

Aristas del árbol de peso mínimo:
(3, 0, 1)
(0, 2, 2)
(1, 2, 4)
```


```Julia
> -  Programa 05: Dijkstra con Heaps Binomiales
```

```Haskell
                 3
              B─────D
            1╱│╲    │╲1
            ╱ │ ╲1  │ ╲
           A 2│  ╲  │2 F
            ╲ │   ╲ │ ╱
            2╲│    ╲│╱1
              C─────E
                 1       

```

```Julia
\src> python Programa05.py Ejemplo.txt A F
----------------------------------------------
Iteracion:  1
Heap:
Orden 0: (0, 'A') Nodo actual: A
Distancia actual: 0
Distancias: {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
----------------------------------------------
Iteracion:  2
Heap:
Orden 1: (1, 'B') (2, 'C') Nodo actual: B
Distancia actual: 1
Distancias: {'A': 0, 'B': 1, 'C': 2, 'D': inf, 'E': inf, 'F': inf}
----------------------------------------------
Iteracion:  3
Heap:
Orden 0: (2, 'E') Orden 1: (2, 'C') (4, 'D') Nodo actual: C
Distancia actual: 2
Distancias: {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 2, 'F': inf}
----------------------------------------------
Iteracion:  4
Heap:
Orden 1: (2, 'E') (4, 'D') Nodo actual: E
Distancia actual: 2
Distancias: {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 2, 'F': inf}
----------------------------------------------
Iteracion:  5
Heap:
Orden 1: (3, 'F') (4, 'D') Nodo actual: F
Distancia actual: 3
Distancias: {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 2, 'F': 3}
----------------------------------------------
Ruta más corta: ['A', 'B', 'E', 'F']
El camino más corto de A a F es: (3, ['A', 'B', 'E', 'F'])
```




Ya que este fue un curso sobre el análisis de algoritmos, las practicas fueron orientadas a la implementacion de varios topicos referentes al tema, como lo es
la implementacion del problema matematico del adoquinamiento, la busqueda binaria de un indice especial, el ordenamiento de los pixeles de una imagen, el bosque generador de peso mínimo
de una grafica disconexa o la implementacion de el algoritmo de Dijkstra con una estructura de datos nada usual como los Heaps Binomiales.

Para poder correr los programas que usan **Java** vamos a necesitar de la ultima version posible de [JAVA](https://www.oracle.com/java/technologies/downloads/), esto con 
el fin de evitar problemas de compatibilidad (se recomienda openjdk 20.0.2 o superiores).

Para poder correr los programas que usan **Python** vamos a necesitar de la ultima version posible de [PYTHON](https://www.python.org/downloads/), esto con 
el fin de evitar problemas de compatibilidad (se recomienda Python 3.11.4 o superiores).

En caso de problemas de compatibilidad en **Python** con las paqueteria de networkx, matplotlib o imageio

Es recomendable correr los siguientes comandos para asegurarnos que tenemos instalado lo anterior en nuestra instalacion de **Python**:

```Haskell
C:\Users\C> pip install networkx matplotlib
```


```Haskell
C:\Users\C> pip install imageio
```


