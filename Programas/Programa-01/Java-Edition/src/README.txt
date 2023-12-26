Del siguiente problema se plantea programarlo en Java y tener dos paquetes de clases, el primero se
dedica al funcionamiento del problema (el algoritmo de adoquinamiento)
el segundo paquete se dedica a la construccion visual de el problema.


Problema del adoquinamiento
Se desea adoquinar una cuadricula de m × m con adoquines en

forma de “L”, como el siguiente:

|----|----|
| *  |    |
|----|----|
| *  | *  |
|----|----|

Las condiciones son las siguientes:
● m = 2^k es decir m debe ser potencia de 2.

● En la cuadricula existirá un “cuadro especial” que será puesto de
manera arbitraria en la cuadricula y no podrá ser cubierto por
ninguna otra pieza.

|----|----|
|    | e  |
|----|----|
|    |    |
|----|----|

Descripción:
El programa a implementar recibe como entrada en los argumentos
de la línea de comandos (ejecutando desde la carpeta ’src’) un entero
positivo k, el cuál indicará el tamaño de nuestra cuadricula a
adoquinar.
Ejemplos de la entrada:
java main 2

|----|----|
| *  | e  |
|----|----|
| *  | *  |
|----|----|



