def busqueda_binaria_conHist(lista, elemento):
    inicio = 0
    fin = len(lista) - 1
    iteraciones = 0

    print(f"Elemento buscado: {elemento}")
    print(f"Espacio de busqueda inicial: {lista[inicio:fin + 1]}")

    while inicio <= fin:
        medio = (inicio + fin) // 2
        iteraciones += 1

        if lista[medio] == elemento:
            print(f"Elemento encontrado en el indice {medio}.")
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

# Ejemplo de uso
lista_ordenada = [2, 3, 1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 5, 61, 67, 71, 73, 79, 83, 89, 97]
elemento_buscado = 71
resultado = busqueda_binaria_conHist(lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el indice {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")