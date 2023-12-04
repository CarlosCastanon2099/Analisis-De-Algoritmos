import sys 
import networkx as nx


class Grafica:
    def __init__(self, vertices):
        self.vertices = vertices
        self.aristas = []

    def agregarArista(self, u, v, peso):
        self.aristas.append((u, v, peso))

    def obtenerAristas(self):
        return sorted(self.aristas, key=lambda arista: arista[2])

    def is_directed(self):
        for u, v, peso in self.aristas:
            if (v, u, peso) not in self.aristas:
                return False
        return True

    def generadorDeArbolDePesoMinimo(self):
        arbol_peso_minimo = Grafica(self.vertices)
        conjunto_disjoint = {v: {v} for v in range(self.vertices)}

        for arista in self.obtenerAristas():
            u, v, peso = arista

            conjunto_u = conjunto_disjoint[u]
            conjunto_v = conjunto_disjoint[v]

            if conjunto_u != conjunto_v:
                arbol_peso_minimo.agregarArista(u, v, peso)

                # Unir los conjuntos
                conjunto_u.update(conjunto_v)

                for vertex in conjunto_v:
                    conjunto_disjoint[vertex] = conjunto_u

        return arbol_peso_minimo


class Arista:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __repr__(self):
        return f"({self.u}, {self.v}, {self.peso})"

class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = {}

    def agregarVecino(self, id, peso):
        self.vecinos[id] = peso

    def obtenerVecinos(self):
        return self.vecinos.keys()

    def obtenerPeso(self, id):
        return self.vecinos[id]

    def __repr__(self):
        return f"({self.id}, {self.vecinos})"


# Ejemplo de uso:
# Supongamos que g es una instancia de la clase Grafica con aristas agregadas.
"""
g = Grafica(5)
g.agregarArista(0, 1, 2)
g.agregarArista(0, 2, 4)
g.agregarArista(1, 2, 1)
g.agregarArista(1, 3, 5)
g.agregarArista(2, 3, 8)

arbol_peso_minimo = g.generadorDeArbolDePesoMinimo()

print("Aristas del árbol de peso mínimo:")
for arista in arbol_peso_minimo.obtenerAristas():
    print(arista)
"""



# Ahora, imaginemos que tenemos una grafica disconexa con 2 o mas componentes conexas
g2 = Grafica(9)
g2.agregarArista(0, 1, 1)
g2.agregarArista(1, 3, 3)
g2.agregarArista(2, 1, 3)
g2.agregarArista(3, 2, 5)
g2.agregarArista(4, 0, 3)
g2.agregarArista(5, 6, 4)
g2.agregarArista(6, 7, 5)
g2.agregarArista(7, 8, 1)
g2.agregarArista(8, 6, 2) 


# Y de esta grafica queremos saber, cuantas componentes conexas tiene para que de esa forma
# A cada componente conexa le apliquemos la funcion generadorDeArbolDePesoMinimo y asi obtener
# El arbol de peso minimo de cada componente conexa.

# Para esto, usaremos la funcion de networkx, connected_components, la cual nos devuelve un
# generador de conjuntos de vertices, donde cada conjunto representa una componente conexa.
# Por ejemplo, si tenemos 3 componentes conexas, el generador nos devolvera 3 conjuntos de vertices,
# donde cada conjunto representa una componente conexa.

def convertir_a_networkx_graph(g):
    G = nx.Graph()
    for u, v, peso in g.obtenerAristas():
        G.add_edge(u, v, weight=peso)
    return G

def obtenerComponentesConexas(g):
    G = convertir_a_networkx_graph(g)
    componentes_conexas = nx.connected_components(G)
    return componentes_conexas


# Ahora, para cada componente conexa, le aplicaremos la funcion generadorDeArbolDePesoMinimo
# y asi obtener el arbol de peso minimo de cada componente conexa.
def obtenerArbolesDePesoMinimoDeCadaComponenteConexa(g):
    componentes_conexas = obtenerComponentesConexas(g)
    arboles_de_peso_minimo = []
    for componente_conexa in componentes_conexas:
        mapeo_vertices = {v: i for i, v in enumerate(componente_conexa)}
        g_componente_conexa = Grafica(len(componente_conexa))
        for arista in g.obtenerAristas():
            u, v, peso = arista
            if u in componente_conexa and v in componente_conexa:
                g_componente_conexa.agregarArista(mapeo_vertices[u], mapeo_vertices[v], peso)
        try:
            arboles_de_peso_minimo.append(g_componente_conexa.generadorDeArbolDePesoMinimo())
        except KeyError as e:
            print(f"El vértice {e} no existe en la gráfica original.")
    return arboles_de_peso_minimo


# Funcion toString para imprimir el arbol de peso minimo de cada componente conexa
def toString(arboles_de_peso_minimo):
    for arbol in arboles_de_peso_minimo:
        print("Aristas del árbol de peso mínimo:")
        for arista in arbol.obtenerAristas():
            print(arista)
        print()


# Ejemplo de uso:
arboles_de_peso_minimo = obtenerArbolesDePesoMinimoDeCadaComponenteConexa(g2)
toString(arboles_de_peso_minimo)