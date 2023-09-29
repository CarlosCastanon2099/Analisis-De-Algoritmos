def busqueda_binaria(lista, elemento):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio  # Elemento encontrado, devuelve el índice.
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  # Elemento no encontrado, devuelve -1.

# Ejemplo de uso
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_buscado = 11
resultado = busqueda_binaria(lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")