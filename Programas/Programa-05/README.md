<div align="center">

# 🤖 **Programa 5** 🛸



# **Dijkstra con Heaps Binomiales.**


</div>


<div align="center">

[![](https://media.giphy.com/media/v7onhWkADN32g/giphy.gif)](https://www.youtube.com/watch?v=0J2QdDbelmY)

</div>


---

## **Uso**

Para correr el programa que genera el camino mas corto entre un vertice $v$ y uno $u$ paso a paso en una Grafica arbitraria conexa $G=(V,E)$ (en donde $v \neq u$), usando
el algoritmo de **Dijkstra** con la estructura de datos de **Heaps Binomiales (Colas Binomiales)**.
- Compilar desde `src/`:

Linux  : 

```Haskell
\src> python3 Programa05.py <archivo_grafica.txt> <nodo_inicial> <nodo_final>
```

Windows:  

```Python
\src> python Programa05.py <archivo_grafica.txt> <nodo_inicial> <nodo_final>
```

Para el funcionamiento del programa, se debe proporcionar un archivo **.txt** (el cual debe estar en src), el **.txt**
debe contener una grafica conexa (el programa tambien funciona con graficas disconexas pero recordemos que en una grafica 
disconexa podría darse el caso en el que no exista un camino entre dos vertices arbitrarios $v$ y uno $u$), la grafica en el archivo **.txt**, debe cumplir con:

- En la primera línea tendrá todos los vértices que forman a la Grafica, separados por una coma (’,’).

- En las siguientes líneas irán pares de vértices, separados por una coma (’,’), que indicará en las
aristas de la Grafica, seguido de dos puntos (‘ : ’) para indicar el peso de la arista.

- Nota: Los vertices pueden ser caracteres alfa numericos (no necesariamente solo letras, pero el seguimiento del algoritmo nombrando a los vertices por numeros puede ser un poco mas complicado en Graficas grandes).

Teniendo de ejemplo de esto a:

```Haskell
A,B,C,D,E,F
A,B:1
A,C:2
B,A:1
B,C:2
B,D:3
B,E:1
C,A:2
C,B:2
C,E:1
D,B:3
D,E:2
D,F:1
E,C:1
E,D:2
E,F:1
E,B:1
F,D:1
F,E:1
```

La cual es la representacion de la grafica:

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


----

# **Ejemplo de uso**

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


--------

# **Conceptos sobre Graficas**


```Python
Gráfica:
```

Sea $G = (V, E)$, donde $V$ es un conjunto de nodos (vértices) y $E$ es un conjunto de aristas que conecta pares de nodos, esta será una Grafica.



```Python
Gráfica Conexa:
```

Una gráfica $G = (V, E)$ es conexa si, para cada par de nodos $u, v \in V$, existe al menos un camino en $E$ que conecta $u$ con $v$.



```Python
Gráfica Disconexa:
```

Una gráfica $G = (V, E)$ es disconexa si puede ser descompuesta en dos o más conjuntos de nodos no vacíos $V_1, V_2, \ldots, V_k$ 
tales que no hay aristas en $E$ que conecten nodos de conjuntos diferentes $V_i$.


```Python
Ruta Más Corta:
```

La ruta más corta entre dos vértices $v$ y $u$ en una grafica es el camino que minimiza la suma de los pesos de las aristas a lo largo de ese camino. 
En otras palabras, es la ruta que tiene la menor longitud posible en términos de la suma de los pesos de las aristas.


```Haskell
Algoritmo de Dijkstra:
```

El algoritmo de Dijkstra es un algoritmo de búsqueda de caminos más cortos en una grafica ponderada con pesos no negativos. 
Su objetivo es encontrar la distancia más corta desde un vértice de origen (inicial) hasta un vertice de destino (final). 
El algoritmo mantiene una lista de distancias tentativas desde el vértice de origen hacia todos los demás vértices y se actualiza a medida que encuentra caminos más cortos.

**Pasos:**
1. **Inicialización:** Asigna una distancia tentativa de cero al vértice de origen y de infinito a todos los demás vértices.
2. **Exploración:** Explora los vértices adyacentes al vértice actual, actualizando las distancias tentativas si encuentra un camino más corto.
3. **Selección:** Selecciona el vértice no visitado con la distancia tentativa más corta como el próximo vértice actual y repite el proceso hasta que todos los vértices han sido visitados.

El resultado final es el conjunto de distancias más cortas desde el vértice de origen hasta el vertice de destino.
