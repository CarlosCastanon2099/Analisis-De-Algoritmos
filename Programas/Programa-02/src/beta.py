def busqueda_binaria_indice_especial(lista):
    print(f"Espacio de búsqueda inicial: {lista}")
    def busqueda_especial(i_izq, i_der):
        iteraciones = 0
        print(f"Iteracion {iteraciones}: Espacio de busqueda: {lista[i_izq - 1:i_der]}")
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

    #print(f"Índice especial encontrado en el índice {indice_especial}: {lista[indice_especial - 1]}" )
    print(f"Número total de iteraciones: {iteraciones}")
    return indice_especial


# Ejemplo de uso
lista_ordenada = [-5, -4, -2, 0, 1, 3, 5, 7, 8, 9, 11, 13, 14, 15, 16]
indice_especial = busqueda_binaria_indice_especial(lista_ordenada)

if indice_especial is not None:
    print(f"Indice especial encontrado en el indice {indice_especial}: {lista_ordenada[indice_especial - 1]}")
else:
    print("No se encontro ningun indice especial en la lista.")