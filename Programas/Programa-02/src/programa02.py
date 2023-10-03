import sys

# Metodo busqueda_binaria_indice_especial 
def busqueda_binaria_indice_especial(lista):
# PreCondiciones: lista es una lista de numeros enteros ordenados, finita y no vacia
# PostCondiciones: Si elemento se encuentra en lista, se regresa el indice de elemento en lista y nos 
#                  indica el numero de iteraciones que se realizaron para encontrarlo, en caso contario solo
#                  nos indica que no se encontro el elemento y el numero de iteraciones que se realizaron.

    def busqueda_especial(i_izq, i_der):
        # Pendiente 
        # print(f"Iteracion {iteraciones}: Espacio de busqueda: {lista[i_izq - 1:i_der]}")
        print(f"Espacio de busqueda: {lista[i_izq - 1:i_der]}")
        if i_izq == i_der:
            if lista[i_izq - 1] == i_izq:
                return i_izq, 1
            else:
                return -1, 1
        else:
            mitad = (i_izq + i_der) // 2
            if lista[mitad - 1] < mitad:
                indice, iteraciones = busqueda_especial(mitad + 1, i_der)
            else:
                indice, iteraciones = busqueda_especial(i_izq, mitad)
            return indice, iteraciones + 1
            
    indice_especial, iteraciones = busqueda_especial(1, len(lista))

    # print(f"Indice especial encontrado en el indice {indice_especial}: {lista[indice_especial - 1]}" ) 
    # Por alguna extraña razon lo de arriba imprime todas las iteraciones pero en sentido inverso 

    print(f"Número total de iteraciones: {iteraciones}")

    if indice_especial != -1:
        print(f"Indice especial encontrado en el indice {indice_especial}: {lista[indice_especial - 1]}")
    else:
        print("No se encontro ningun indice especial en la lista.")
    
    return indice_especial
    


# Metodo main
def main():
    if len(sys.argv) != 2:
        print("\n Error en los argumentos \n Uso Linux: python3 programa02.py <nombreArchivo.txt> \n Uso Windows: python programa02.py <nombreArchivo.txt>  \n ")
        sys.exit(1)
    else:
        try: # Try - Catch para manejar los errores del programa
            with open(sys.argv[1], "r") as archivo:
                lista = [int (numero) for numero in archivo.read().split(",")]

            resultado = busqueda_binaria_indice_especial(lista)
        except FileNotFoundError:
            print(f"\n El archivo {sys.argv[1]} no existe. \n")
            sys.exit(1)
        except ValueError:
            print(f"\n El archivo no contiene elementos, hay algo que no es un numero entero o no se esta usando el formato; 1,2,3,...,n  \n Error en los argumentos \n Uso Linux: python3 programa02.py <nombreArchivo.txt>  \n Uso Windows: python programa02.py <nombreArchivo.txt>  \n ")
            sys.exit(1)
        except: # Cualquier otro error
            print(f"\n En el nombre de la Trifuerza como llegaste aqui ._. ? \n Error inesperado: {sys.exc_info()[0]} \n")
            sys.exit(1)
        
        #if resultado is not None:
        #    print(f"Indice especial encontrado en el indice {resultado}: {lista[resultado - 1]}")
        #else:
        #    print("No se encontro ningun indice especial en la lista.")

if __name__ == "__main__":
    main()