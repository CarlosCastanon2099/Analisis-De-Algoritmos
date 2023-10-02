def busqueda_binaria_indice_especial(lista):
    def busqueda_especial(i_izq, i_der):
        if i_izq == i_der:
            if lista[i_izq - 1] == i_izq:
                return i_izq
            else:
                return None
        else:
            mitad = (i_izq + i_der) // 2
            if lista[mitad - 1] < mitad:
                return busqueda_especial(mitad + 1, i_der)
            else:
                return busqueda_especial(i_izq, mitad)

    return busqueda_especial(1, len(lista))

# Ejemplo de uso
lista_ordenada = [-5, -4, -2, 0, 1, 3, 5, 7, 8, 9, 11, 13, 14, 15, 16]
indice_especial = busqueda_binaria_indice_especial(lista_ordenada)

if indice_especial is not None:
    print(f"Indice especial encontrado en el indice {indice_especial}: {lista_ordenada[indice_especial - 1]}")
else:
    print("No se encontro ningun indice especial en la lista.")