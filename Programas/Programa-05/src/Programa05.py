class NodoBinomial:
    def __init__(self, valor):
        self.valor = valor
        self.grado = 0
        self.hijos = []
        self.padre = None
        self.hermano_derecho = None


class HeapBinomial:
    def __init__(self):
        self.raiz = None

    def agregar_elemento(self, valor):
        nuevo_nodo = NodoBinomial(valor)
        heap_temporal = HeapBinomial()
        heap_temporal.raiz = nuevo_nodo
        self.mezclar(heap_temporal)

    def eliminar_elemento(self, valor):
        if self.raiz is None:
            return
        nodo = self.buscar_nodo(valor)
        if nodo is None:
            return
        self.decrementar_llave(nodo, float('-inf'))
        self.extraer_minimo()

    def mezclar(self, heap):
        self.unir_heaps(heap)
        if self.raiz is None:
            return
        nodo_previo = None
        nodo_actual = self.raiz
        nodo_siguiente = nodo_actual.hermano_derecho
        while nodo_siguiente is not None:
            if (nodo_actual.grado != nodo_siguiente.grado or
                    (nodo_siguiente.hermano_derecho is not None and
                     nodo_siguiente.hermano_derecho.grado == nodo_actual.grado)):
                nodo_previo = nodo_actual
                nodo_actual = nodo_siguiente
            elif nodo_actual.valor <= nodo_siguiente.valor:
                nodo_actual.hermano_derecho = nodo_siguiente.hermano_derecho
                self.enlazar(nodo_siguiente, nodo_actual)
            else:
                if nodo_previo is None:
                    self.raiz = nodo_siguiente
                else:
                    nodo_previo.hermano_derecho = nodo_siguiente
                self.enlazar(nodo_actual, nodo_siguiente)
                nodo_actual = nodo_siguiente
            nodo_siguiente = nodo_actual.hermano_derecho

    def enlazar(self, nodo1, nodo2):
        nodo1.padre = nodo2
        nodo1.hermano_derecho = nodo2.hijos
        nodo2.hijos = nodo1
        nodo2.grado += 1

    def buscar_nodo(self, valor):
        if self.raiz is None:
            return None
        cola = [self.raiz]
        while len(cola) > 0:
            nodo = cola.pop(0)
            if nodo.valor == valor:
                return nodo
            cola.extend(nodo.hijos)
        return None

    def decrementar_llave(self, nodo, nuevo_valor):
        if nodo is None or nodo.valor < nuevo_valor:
            return
        nodo.valor = nuevo_valor
        while nodo.padre is not None and nodo.valor < nodo.padre.valor:
            nodo.valor, nodo.padre.valor = nodo.padre.valor, nodo.valor
            nodo = nodo.padre

    def extraer_minimo(self):
        if self.raiz is None:
            return None
        minimo = self.raiz
        self.raiz = self.unir_arboles(self.raiz.hermano_derecho, self.raiz.hijos)
        return minimo.valor

    def unir_heaps(self, heap):
        self.raiz = self.unir_arboles(self.raiz, heap.raiz)
        heap.raiz = None

    def unir_arboles(self, arbol1, arbol2):
        if arbol1 is None:
            return arbol2
        if arbol2 is None:
            return arbol1
        if arbol1.grado < arbol2.grado:
            arbol1.hermano_derecho = self.unir_arboles(arbol1.hermano_derecho, arbol2)
            return arbol1
        else:
            arbol2.hermano_derecho = self.unir_arboles(arbol2.hermano_derecho, arbol1)
            return arbol2

    def imprimir_heap(self):
        if self.raiz is None:
            print("Heap Binomial vacío")
        else:
            self.imprimir_arbol(self.raiz)

    def imprimir_arbol(self, nodo):
        while nodo is not None:
            print(f"Grado {nodo.grado}: {nodo.valor}")
            if nodo.hijos is not None:
                self.imprimir_arbol(nodo.hijos)
            nodo = nodo.hermano_derecho




# Modificación en la función dijkstra
def dijkstra(grafo, nodo_inicial, nodo_final):
    distancias = {}
    padres = {}
    heap = HeapBinomial()
    for nodo in grafo:
        distancias[nodo] = float('inf')
        padres[nodo] = None
        if nodo == nodo_inicial:
            distancias[nodo] = 0
            heap.agregar_elemento((nodo, distancias[nodo]))
    distancias[nodo_inicial] = 0
    heap.mezclar(heap)
    while heap.raiz is not None and heap.raiz != nodo_final:
        nodo = heap.extraer_minimo()
        for vecino in grafo[nodo]:
            nueva_distancia = distancias[nodo] + grafo[nodo][vecino]
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                padres[vecino] = nodo
                heap.decrementar_llave((vecino, distancias[vecino]), nueva_distancia)
    return distancias, padres



# Demostracion de dijkstra con la siguiente grafica:
"""
                 3
              b─────d
            1╱│╲    │╲1
            ╱ │ ╲1  │ ╲
           a 2│  ╲  │2 f
            ╲ │   ╲ │ ╱
            2╲│    ╲│╱1
              c─────e
                 1       
"""

graficaPrueba = {
    'a': {'b': 1, 'c': 2},
    'b': {'a': 1, 'c': 2, 'd': 3},
    'c': {'a': 2, 'b': 2, 'e': 1},
    'd': {'b': 3, 'e': 2, 'f': 1},
    'e': {'c': 1, 'd': 2, 'f': 1},
    'f': {'d': 1, 'e': 1}
}

distancias, padres = dijkstra(graficaPrueba, 'a', 'f')

print("Distancias:")
print(distancias)
print("Padres:")
print(padres)

print("El camino mas corto de a a f es:")
rutamascorta = dijkstra(graficaPrueba, 'a', 'f')
print(rutamascorta)





