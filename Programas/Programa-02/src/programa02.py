import sys

# Metodo de busqueda binaria con historial
# Realizamos Busqueda Binaria y por cada iteracion vamos imprimiendo el espacio de busqueda 
# y el numero de iteraciones
def busqueda_binaria_conHist(lista, elemento):
# PreCondiciones: lista es una lista de numeros enteros ordenados, finita y no vacia,
#                 elemento es un numero entero finito.
# PostCondiciones: Si elemento se encuentra en lista, se regresa el indice de elemento en lista y nos 
#                  indica el numero de iteraciones que se realizaron para encontrarlo, en caso contario solo
#                  nos indica que no se encontro el elemento y el numero de iteraciones que se realizaron.
    inicio = 0
    fin = len(lista) - 1
    iteraciones = 0


    print(f"Elemento buscado: {elemento}")
    print(f"Espacio de busqueda inicial: {lista[inicio:fin + 1]}")

    while inicio <= fin: # Mientras que el inicio no sea mayor al fin
        medio = (inicio + fin) // 2 # Calculamos el punto medio
        iteraciones += 1 # Aumentamos el numero de iteraciones

        if lista[medio] == elemento: 
            print(f"Elemento encontrado en el indice {medio + 1}.")
            print(f"Numero total de iteraciones: {iteraciones}")
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

        print(f"Iteracion {iteraciones}: Espacio de busqueda: {lista[inicio:fin + 1]}")

    print(f"Elemento {elemento} no encontrado.")
    print(f"Numero total de iteraciones: {iteraciones}")
    return -1

# Metodo main
def main():
    if len(sys.argv) != 3:
        print("\n Error en los argumentos \n Uso Linux: python3 programa02.py <nombreArchivo.txt> <Numero a Buscar> \n Uso Windows: python programa02.py <nombreArchivo.txt> <Numero a Buscar> \n ")
        sys.exit(1)
    else:
        try: # Try - Catch para manejar los errores del programa
            with open(sys.argv[1], "r") as archivo:
                lista = [int (numero) for numero in archivo.read().split(",")]

            elemento = int(sys.argv[2])
            resultado = busqueda_binaria_conHist(lista, elemento)
        except FileNotFoundError:
            print(f"\n El archivo {sys.argv[1]} no existe. \n")
            sys.exit(1)
        except ValueError:
            print(f"\n El archivo no contiene elementos, hay algo que no es un numero entero o no se esta usando el formato; 1,2,3,...,n  \n Error en los argumentos \n Uso Linux: python3 programa02.py <nombreArchivo.txt> <Numero a Buscar> \n Uso Windows: python programa02.py <nombreArchivo.txt> <Numero a Buscar> \n ")
            sys.exit(1)
        except: # Cualquier otro error
            print(f"\n En el nombre de la Trifuerza como llegaste aqui ._. ? \n Error inesperado: {sys.exc_info()[0]} \n")
            sys.exit(1)
        

        if resultado != -1:
            print(f"El elemento {elemento} se encuentra en el indice {resultado + 1}.")
        else:
            print(f"El elemento {elemento} no se encuentra en la lista.")

if __name__ == "__main__":
    main()