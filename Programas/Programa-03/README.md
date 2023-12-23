<div align="center">

# 🚀 **Programa 3** 🌃



# **Ordenamientos**


</div>


<div align="center">

[![](https://media.giphy.com/media/2ysW1pzDWv3SlxFUE3/giphy.gif)](https://www.youtube.com/watch?v=q3yJ_yDhNVk)

</div>


---

## **Uso**

Para correr el programa que realiza el **ordenamiento de los pixeles de una imagen**
- Compilar desde `src/`:

```Haskell
\src> javac sort/Main.java
```

- Correr desde `src/`:

```Haskell
\src> java sort.Main <archivo de resource> <velocidad> <algoritmo>
```

En donde:

```Dart
<archivo de resource> = Nombre de archivo de imagen a procesar, debe encontrarse en la carpeta 'resource'
```

```Kotlin
<velocidad> = Numero de iteraciones que ocurrirán antes de hacer un update a la interfaz grafica
```

```Julia
<algoritmo> = Algoritmo de ordenamiento a utilizar, puede ser:
              'bubble', 'selection', 'insertion', 'merge', 'quick',
              'heap', 'bucket', 'shell', 'radixLSD', 'radixMSD'
```


----

## **Ejemplos de uso**

```Julia
\src> java sort.Main Imagen2.jpg 30 bubble
```

<div align="center">

![Bubble](./../../Media/Bubble-Vel-30.gif)

</div>

```Julia
\src> java sort.Main Imagen3.jpg 75 selection
```

<div align="center">

![Selection](./../../Media/Selection-Vel-75.gif)

</div>


```Julia
\src> java sort.Main Imagen3.jpg 75 insertion
```

<div align="center">

![Insertion](./../../Media/Insertion-Vel-75.gif)

</div>


```Julia
\src> java sort.Main Imagen9.jpg 100 merge
```

<div align="center">

![Merge](./../../Media/Merge-Vel-100.gif)

</div>


```Julia
\src> java sort.Main Imagen4.png 25 quick
```

<div align="center">

![Quick](./../../Media/Quick-Vel-25.gif)

</div>


```Julia
\src> java sort.Main Imagen10.jpg 1 shell
```

<div align="center">

![Shell](./../../Media/Shell-Vel-1.gif)

</div>


```Julia
\src> java sort.Main Imagen2.jpg 1 bucket
```

<div align="center">

![Bucket](./../../Media/Bucket-Vel-1.gif)

</div>


```Julia
\src> java sort.Main Imagen6.jpg 1 heap
```

<div align="center">

![Heap](./../../Media/Heap-Vel-1.gif)

</div>


```Julia
\src> java sort.Main Ultimate.jpg 1 radixLSD
```

<div align="center">

![RadixLSD](./../../Media/RadixLSD-Vel-1.gif)

</div>


```Julia
\src> java sort.Main Ultimate.jpg 1 radixMSD
```

<div align="center">

![RadixMSD](./../../Media/RadixMSD-Vel-1.gif)

</div>
