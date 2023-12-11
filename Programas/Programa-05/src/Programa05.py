import sys 


class ArbolBinomial:
    def __init__(self, key):
        self.key = key
        self.hijos = []
        self.order = 0

    def add_at_end(self, t):
        self.hijos.append(t)
        self.order += 1


class HeapBinomial:
    def __init__(self):
        self.arboles = []

    def extract_min(self):
        if not self.arboles:
            return None
        nodo_minimo = self.arboles[0]
        for tree in self.arboles:
            if tree.key < nodo_minimo.key:
                nodo_minimo = tree
        self.arboles.remove(nodo_minimo)
        h = HeapBinomial()
        h.arboles = nodo_minimo.hijos
        self.merge(h)
        return nodo_minimo.key

    def get_min(self):
        if not self.arboles:
            return None
        return min(tree.key for tree in self.arboles)

    def combinaRaices(self, h):
        self.arboles.extend(h.arboles)
        self.arboles.sort(key=lambda tree: tree.order)

    def merge(self, h):
        self.combinaRaices(h)
        if not self.arboles:
            return
        i = 0
        while i < len(self.arboles) - 1:
            actual = self.arboles[i]
            despues = self.arboles[i + 1]
            if actual.order == despues.order:
                if (i + 1 < len(self.arboles) - 1
                        and self.arboles[i + 2].order == despues.order):
                    despuesDeDespues = self.arboles[i + 2]
                    if despues.key < despuesDeDespues.key:
                        despues.add_at_end(despuesDeDespues)
                        del self.arboles[i + 2]
                    else:
                        despuesDeDespues.add_at_end(despues)
                        del self.arboles[i + 1]
                else:
                    if actual.key < despues.key:
                        actual.add_at_end(despues)
                        del self.arboles[i + 1]
                    else:
                        despues.add_at_end(actual)
                        del self.arboles[i]
            i += 1

    def insert(self, key):
        g = HeapBinomial()
        g.arboles.append(ArbolBinomial(key))
        self.merge(g)
    
    def display(self):
        for tree in self.arboles:
            print('Orden {}:'.format(tree.order), end=' ')
            self.display_tree(tree)
    
    def display_tree(self, tree):
        if not tree.hijos:
            print(tree.key, end=' ')
            return
        print(tree.key, end=' ')
        for child in tree.hijos:
            self.display_tree(child)


def dijkstra(graficaaa, nodo_inicial, nodo_final):
    distancias = {}
    padres = {}
    heap = HeapBinomial()

    for nodo in graficaaa:
        distancias[nodo] = float('inf')
        padres[nodo] = None

    distancias[nodo_inicial] = 0
    heap.insert((0, nodo_inicial))
    iteracion = 0

    while heap.arboles:
        iteracion += 1
        # Imprimimos en que iteracion estamos
        print("----------------------------------------------")
        print("Iteracion: ", iteracion)
        print("Heap:")
        heap.display()
        distancia_actual, nodo = heap.extract_min()
        print("Nodo actual:", nodo)
        print("Distancia actual:", distancia_actual)
        print("Distancias:", distancias)

        if nodo == nodo_final:
            break

        for vecino, peso in graficaaa[nodo].items():
            nueva_distancia = distancias[nodo] + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                padres[vecino] = nodo
                heap.insert((nueva_distancia, vecino))

    # Reconstruimos la ruta más corta
    ruta_mas_corta = []
    actual = nodo_final
    while actual is not None:
        ruta_mas_corta.insert(0, actual)
        actual = padres[actual]
    
    print("----------------------------------------------")
    # Imprimimos la ruta más corta
    print("Ruta más corta:", ruta_mas_corta)


    return distancias[nodo_final], ruta_mas_corta



"""
# Demostracion de dijkstra con la siguiente grafica:

                 3
              b─────d
            1╱│╲    │╲1
            ╱ │ ╲1  │ ╲
           a 2│  ╲  │2 f
            ╲ │   ╲ │ ╱
            2╲│    ╲│╱1
              c─────e
                 1       


graficaPrueba = {
    'a': {'b': 1, 'c': 2},
    'b': {'a': 1, 'c': 2, 'd': 3, 'e': 1},
    'c': {'a': 2, 'b': 2, 'e': 1},
    'd': {'b': 3, 'e': 2, 'f': 1},
    'e': {'c': 1, 'd': 2, 'f': 1, 'b': 1},
    'f': {'d': 1, 'e': 1}
}

ruta_mas_corta = dijkstra(graficaPrueba, 'a', 'f')
print("El camino más corto de 'a' a 'f' es:", ruta_mas_corta)

"""

# Ahora, como nos interesa el leer la grafica desde un archivo de texto que nos pasen por consola
# tenemos el siguiente metodo que primero lee el archivo de texto
def leerArchivo(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    archivo.close()
    return lineas

# Los archivos que vamos a leer son de la forma:
"""
- En la primera línea tendrá todos los vértices que forman a G,
separados por una coma (’,’).
- En las siguientes líneas irán pares de vértices, separados por una
coma (’,’), que indicará en las aristas de G, seguido de dos puntos
(‘ : ’) para indicar el peso de la arista.
Teniendo de ejemplo de esto a:
A,B,C,D,E,F
A,B:1
A,C:2
B,A:1
B,C:2
B,D:3
B,E:1
C,A:2
C,B:2
C,E:1
D,B:3
D,E:2
D,F:1
E,C:1
E,D:2
E,F:1
E,B:1
F,D:1
F,E:1

"""

# Ya que con el metodo anterior leemos el archivo, ahora tenemos que crear la grafica
# con los datos que nos da el archivo de texto.
# La grafica que vamos a crear debe ser de esta forma:
"""
graficaPrueba = {
    'a': {'b': 1, 'c': 2},
    'b': {'a': 1, 'c': 2, 'd': 3, 'e': 1},
    'c': {'a': 2, 'b': 2, 'e': 1},
    'd': {'b': 3, 'e': 2, 'f': 1},
    'e': {'c': 1, 'd': 2, 'f': 1, 'b': 1},
    'f': {'d': 1, 'e': 1}
}

y la que recibimos del .txt es:
A,B,C,D,E,F
A,B:1
A,C:2
B,A:1
B,C:2
B,D:3
B,E:1
C,A:2
C,B:2
C,E:1
D,B:3
D,E:2
D,F:1
E,C:1
E,D:2
E,F:1
E,B:1
F,D:1
F,E:1
"""

def read_graph_from_file(file_path):
    grafica = {}
    with open(file_path, 'r') as file:
        # Lee la primera línea para obtener los vértices
        vertices = file.readline().strip().split(',')
        for vertex in vertices:
            grafica[vertex] = {}

        # Lee las siguientes líneas para obtener las aristas y pesos
        for line in file:
            data = line.strip().split(':')
            vertices, peso = data[0], int(data[1])
            origen, destino = vertices.split(',')
            grafica[origen][destino] = peso

    return grafica

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python Programa05.py <archivo_grafica.txt> <nodo_inicial> <nodo_final>")
        sys.exit(1)
    
    nombreArchivo = sys.argv[1]
    nodoInicial = sys.argv[2]
    nodoFinal = sys.argv[3]

    grafica = read_graph_from_file(nombreArchivo)
    ruta_mas_corta = dijkstra(grafica, nodoInicial, nodoFinal)
    print("El camino más corto de", nodoInicial, "a", nodoFinal, "es:", ruta_mas_corta)
