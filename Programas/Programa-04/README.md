<div align="center">

# 🌳 **Programa 4** ❄️



# **Bosque Generador de Peso Mínimo.**


</div>


<div align="center">

[![](https://media.giphy.com/media/RWJPtq90qOA4E/giphy.gif)](https://www.youtube.com/watch?v=o1tj2zJ2Wvg)

</div>


---

## **Uso**

Para correr el programa que genera el **Bosque Generador de Peso Mínimo** de una grafica disconexa.
- Compilar desde `src/`:

Linux  : 

```Haskell
\src> python3 Programa04.py <nombre.txt>
```

Windows:  

```Python
\src> python Programa04.py <nombre.txt>
```

Para el funcionamiento del programa, se debe proporcionar un archivo **.txt** (el cual debe estar en src), el **.txt**
debe contener una grafica disconexa (el programa tambien funciona con graficas conexas pero recordemos que en una grafica 
conexa solo obtendriamos un arbol de peso minimo), la grafica en el archivo **.txt**, debe cumplir con:

- En la primera línea tendrá todos los vértices que forman a la Grafica, separados por una coma (’,’).

- En las siguientes líneas irán pares de vértices, separados por una coma (’,’), que indicará en las
aristas de la Grafica, seguido de dos puntos (‘ : ’) para indicar el peso de la arista.

Teniendo de ejemplo de esto a:

```Haskell
0,1,2,3,4,5,6,7,8
0,1:1
1,3:3
2,1:3
3,2:5
4,0:3
5,6:4
6,7:5
7,8:1
8,6:2
```


----

# **Ejemplo de uso**

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


----

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
Árbol de Peso Mínimo:
```

Dada una gráfica ponderada $G = (V, E, w)$, donde $w: E \rightarrow \mathbb{R}$ asigna pesos (weights) a las aristas, un árbol de peso mínimo 
es un subconjunto de aristas $T \subseteq E$ tal que $T$ forma un árbol (sin ciclos) que conecta todos los nodos en $V$, y la suma de 
los pesos de $T$ es la mínima posible.



```Python
Bosque de Árboles de Peso Mínimo:
```

Dada una gráfica ponderada $G = (V, E, w)$, un bosque de árboles de peso mínimo es una colección de árboles de peso mínimo $T_1, T_2, \ldots, T_k$ 
que cubren todos los nodos en $V$ sin formar ciclos. Cada $T_i$ es un árbol de peso mínimo en $G$.

