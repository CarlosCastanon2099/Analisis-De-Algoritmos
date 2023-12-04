package clases;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * Clase para gráficas. Una gráfica es un conjunto de vértices y aristas, tales
 * que las aristas son un subconjunto del producto cruz de los vértices.
 */
public class Grafica<T> implements Coleccion<T> {



    /* Clase interna privada para iteradores. */
    public class Iterador implements Iterator<T> {

        /* Iterador auxiliar. */
        private Iterator<Vertice> iterador;

        /* Construye un nuevo iterador, auxiliándose de la lista de vértices. */
        public Iterador() {
            // Aquí va su código.
            iterador = vertices.iterator();
        }

        /* Nos dice si hay un siguiente elemento. */
        @Override public boolean hasNext() {
            // Aquí va su código.
            return iterador.hasNext();
        }

        /* Regresa el siguiente elemento. */
        @Override public T next() {
            // Aquí va su código.
            return iterador.next().elemento;
        }


        
    }

    /* Clase interna privada para vértices. */
    public class Vertice implements VerticeGrafica<T>,
                          ComparableIndexable<Vertice> {

        /* El elemento del vértice. */
        private T elemento;
        /* El color del vértice. */
        private Color color;
        /* La distancia del vértice. */
        private double distancia;
        /* El índice del vértice. */
        private int indice;
        /* El diccionario de vecinos del vértice. */
        public Diccionario<T, Vecino> vecinos;

        /* Crea un nuevo vértice a partir de un elemento. */
        public Vertice(T elemento) {
            // Aquí va su código.
            this.elemento = elemento;
            color = Color.NINGUNO;
            vecinos = new Diccionario<>();
        }

        /* Regresa el elemento del vértice. */
        @Override public T get() {
            // Aquí va su código.
            return elemento;
        }

        /* Regresa el grado del vértice. */
        @Override public int getGrado() {
            // Aquí va su código.
            return vecinos.getElementos();
        }

        /* Regresa el color del vértice. */
        @Override public Color getColor() {
            // Aquí va su código.
            return color;
        }

        /* Regresa un iterable para los vecinos. */
        @Override public Iterable<? extends VerticeGrafica<T>> vecinos() {
            // Aquí va su código.
            return vecinos;
        }

        /* Define el índice del vértice. */
        @Override public void setIndice(int indice) {
            // Aquí va su código.
            this.indice = indice;
        }

        /* Regresa el índice del vértice. */
        @Override public int getIndice() {
            // Aquí va su código.
            return indice;
        }

        /* Compara dos vértices por distancia. */
        @Override public int compareTo(Vertice vertice) {
            // Aquí va su código.
            return Double.compare(distancia, vertice.distancia);
        }

        @Override
        public String toString() {
            return String.valueOf(elemento);
        }
    }

    /* Clase interna privada para vértices vecinos. */
    public class Vecino implements VerticeGrafica<T> {

        /* El vértice vecino. */
        public Vertice vecino;
        /* El peso de la arista conectando al vértice con su vértice vecino. */
        public double peso;

        /* Construye un nuevo vecino con el vértice recibido como vecino y el
         * peso especificado. */
        public Vecino(Vertice vecino, double peso) {
            // Aquí va su código.
            this.vecino = vecino;
            this.peso = peso;
        }

        /* Regresa el elemento del vecino. */
        @Override public T get() {
            // Aquí va su código.
            return vecino.elemento;
        }

        /* Regresa el grado del vecino. */
        @Override public int getGrado() {
            // Aquí va su código.
            return vecino.getGrado();
        }

        /* Regresa el color del vecino. */
        @Override public Color getColor() {
            // Aquí va su código.
            return vecino.color;
        }

        /* Regresa un iterable para los vecinos del vecino. */
        @Override public Iterable<? extends VerticeGrafica<T>> vecinos() {
            // Aquí va su código.
            return vecino.vecinos;
        }

        
        

        

    }

    /* Interface para poder usar lambdas al buscar el elemento que sigue al
     * reconstruir un camino. */
    @FunctionalInterface
    private interface BuscadorCamino<T> {
        /* Regresa true si el vértice se sigue del vecino. */
        public boolean seSiguen(Grafica<T>.Vertice v, Grafica<T>.Vecino a);
    }

    /* Vértices. */
    private Diccionario<T, Vertice> vertices;
    /* Número de aristas. */
    private int aristas;

    /**
     * Constructor único.
     */
    public Grafica() {
        // Aquí va su código.
        vertices = new Diccionario<>();
    }

    /**
     * Regresa el número de elementos en la gráfica. El número de elementos es
     * igual al número de vértices.
     * @return el número de elementos en la gráfica.
     */
    @Override public int getElementos() {
        // Aquí va su código.
        return vertices.getElementos();
    }

    /**
     * Regresa el número de aristas.
     * @return el número de aristas.
     */
    public int getAristas() {
        // Aquí va su código.
        return aristas;
    }

    /**
     * Agrega un nuevo elemento a la gráfica.
     * @param elemento el elemento a agregar.
     * @throws IllegalArgumentException si el elemento ya había sido agregado a
     *         la gráfica.
     */
    @Override public void agrega(T elemento) {
        // Aquí va su código.
        if(elemento == null || contiene(elemento)){
            throw new IllegalArgumentException();
        }
        
        Vertice vertice = new Vertice(elemento);
        vertices.agrega(elemento, vertice);
    }



    /**
     * Conecta dos elementos de la gráfica. Los elementos deben estar en la
     * gráfica. El peso de la arista que conecte a los elementos será 1.
     * @param a el primer elemento a conectar.
     * @param b el segundo elemento a conectar.
     * @throws NoSuchElementException si a o b no son elementos de la gráfica.
     * @throws IllegalArgumentException si a o b ya están conectados, o si a es
     *         igual a b.
     */
    public void conecta(T a, T b) {
        // Aquí va su código.
        conecta(a, b, 1);
    }

    /**
     * Conecta dos elementos de la gráfica. Los elementos deben estar en la
     * gráfica.
     * @param a el primer elemento a conectar.
     * @param b el segundo elemento a conectar.
     * @param peso el peso de la nueva vecino.
     * @throws NoSuchElementException si a o b no son elementos de la gráfica.
     * @throws IllegalArgumentException si a o b ya están conectados, si a es
     *         igual a b, o si el peso es no positivo.
     */
    public void conecta(T a, T b, double peso) {
        // Aquí va su código.
        if(a.equals(b) || peso <= 0){
            throw new IllegalArgumentException();
        }

        Vertice verticePrimero = (Vertice) vertice(a);
        Vertice verticeSegundo = (Vertice) vertice(b);

        if(sonVecinos(verticePrimero.elemento, verticeSegundo.elemento)){
            throw new IllegalArgumentException();
        }

        verticePrimero.vecinos.agrega(b, (new Vecino(verticeSegundo, peso)));
        verticeSegundo.vecinos.agrega(a, (new Vecino(verticePrimero, peso)));

        aristas++;

    }

    /**
     * Desconecta dos elementos de la gráfica. Los elementos deben estar en la
     * gráfica y estar conectados entre ellos.
     * @param a el primer elemento a desconectar.
     * @param b el segundo elemento a desconectar.
     * @throws NoSuchElementException si a o b no son elementos de la gráfica.
     * @throws IllegalArgumentException si a o b no están conectados.
     */
    public void desconecta(T a, T b) {
        // Aquí va su código.
        Vertice verticePrimero = (Vertice) vertice(a);
        Vertice verticeSegundo = (Vertice) vertice(b);

        if(!sonVecinos(verticePrimero.elemento, verticeSegundo.elemento)){
            throw new IllegalArgumentException();
        }

	    verticePrimero.vecinos.elimina(b);
        verticeSegundo.vecinos.elimina(a);

        aristas--;

    }

    /**
     * Nos dice si el elemento está contenido en la gráfica.
     * @return <code>true</code> si el elemento está contenido en la gráfica,
     *         <code>false</code> en otro caso.
     */
    @Override public boolean contiene(T elemento) {
        // Aquí va su código.
        return vertices.contiene(elemento);

    }

    /**
     * Elimina un elemento de la gráfica. El elemento tiene que estar contenido
     * en la gráfica.
     * @param elemento el elemento a eliminar.
     * @throws NoSuchElementException si el elemento no está contenido en la
     *         gráfica.
     */
    @Override public void elimina(T elemento) {
        // Aquí va su código.

        Vertice vertice = (Vertice) vertice(elemento);

        for(Vecino vecino : vertice.vecinos){
            desconecta(vertice.elemento, vecino.vecino.elemento);
        }
            
        vertices.elimina(elemento);

    }

    /**
     * Nos dice si dos elementos de la gráfica están conectados. Los elementos
     * deben estar en la gráfica.
     * @param a el primer elemento.
     * @param b el segundo elemento.
     * @return <code>true</code> si a y b son vecinos, <code>false</code> en otro caso.
     * @throws NoSuchElementException si a o b no son elementos de la gráfica.
     */
    public boolean sonVecinos(T a, T b) {
        // Aquí va su código.
        Vertice verticePrimero = (Vertice) vertice(a);
        Vertice verticeSegundo = (Vertice) vertice(b);

	    return verticePrimero.vecinos.contiene(b);

    }

    /**
     * Regresa el peso de la arista que comparten los vértices que contienen a
     * los elementos recibidos.
     * @param a el primer elemento.
     * @param b el segundo elemento.
     * @return el peso de la arista que comparten los vértices que contienen a
     *         los elementos recibidos.
     * @throws NoSuchElementException si a o b no son elementos de la gráfica.
     * @throws IllegalArgumentException si a o b no están conectados.
     */
    public double getPeso(T a, T b) {
        // Aquí va su código.
        if(!contiene(a)){
            throw new NoSuchElementException();
        }
            
        Vertice vertice = (Vertice) vertice(b);

        if(!sonVecinos(a, b)){
            throw new IllegalArgumentException();
        }

        return vertice.vecinos.get(a).peso;

    }

    /**
     * Define el peso de la arista que comparten los vértices que contienen a
     * los elementos recibidos.
     * @param a el primer elemento.
     * @param b el segundo elemento.
     * @param peso el nuevo peso de la arista que comparten los vértices que
     *        contienen a los elementos recibidos.
     * @throws NoSuchElementException si a o b no son elementos de la gráfica.
     * @throws IllegalArgumentException si a o b no están conectados, o si peso
     *         es menor o igual que cero.
     */
    public void setPeso(T a, T b, double peso) {
        // Aquí va su código.
        Vertice verticePrimero = (Vertice) vertice(a);
        Vertice verticeSegundo = (Vertice) vertice(b);

        if(peso <= 0){
            throw new IllegalArgumentException();
        }

        if(!sonVecinos(verticePrimero.elemento, verticeSegundo.elemento)){
            throw new IllegalArgumentException();
        }
            

        for(Vecino vecino : verticePrimero.vecinos){
            if(vecino.vecino.equals(verticeSegundo)){
                vecino.peso = peso;
                break;
            }
        }
            

        for(Vecino vecino : verticeSegundo.vecinos){
            if(vecino.vecino.equals(verticePrimero)){
                vecino.peso = peso;
                break;
            }
        }
            
            
    }

    /**
     * Regresa el vértice correspondiente el elemento recibido.
     * @param elemento el elemento del que queremos el vértice.
     * @throws NoSuchElementException si elemento no es elemento de la gráfica.
     * @return el vértice correspondiente el elemento recibido.
     */
    public VerticeGrafica<T> vertice(T elemento) {
        // Aquí va su código.
        for(Vertice vertice : vertices){
            if(vertice.elemento.equals(elemento)){
                return vertice;
            }
            
        }
            
        throw new NoSuchElementException();
    }

    /**
     * Define el color del vértice recibido.
     * @param vertice el vértice al que queremos definirle el color.
     * @param color el nuevo color del vértice.
     * @throws IllegalArgumentException si el vértice no es válido.
     */
    public void setColor(VerticeGrafica<T> vertice, Color color) {
        // Aquí va su código.
        if (vertice == null || (vertice.getClass() != Vertice.class && vertice.getClass() != Vecino.class)){
            throw new IllegalArgumentException();
        }
            

        if(vertice.getClass() == Vertice.class){
            Vertice verticeAux = (Vertice) vertice;
            verticeAux.color = color;
        }

        if(vertice.getClass() == Vecino.class){
            Vecino verticeAux = (Vecino) vertice;
            verticeAux.vecino.color = color;
        }
    }

    /**
     * Nos dice si la gráfica es conexa.
     * @return <code>true</code> si la gráfica es conexa, <code>false</code> en
     *         otro caso.
     */
    public boolean esConexa() {
        // Aquí va su código.
        for(Vertice vertice : vertices){
            recorre(vertice.elemento, e -> {}, new Cola<Vertice>());
            break;
        }

        for(Vertice v : vertices){
            if(v.color == Color.ROJO){
                return false;
            }
        }

        return true;

    }

    private void recorre(T elemento, AccionVerticeGrafica<T> accion, MeteSaca<Vertice> estructura) {
        Vertice vertice = (Vertice) vertice(elemento);

        paraCadaVertice((v) -> setColor(v, Color.ROJO));

        vertice.color = Color.NEGRO;
        estructura.mete(vertice);

        while(!estructura.esVacia()){
            vertice = estructura.saca();
            accion.actua(vertice);

            for(Vecino vecino : vertice.vecinos){
                if(vecino.vecino.color == Color.ROJO){
                    vecino.vecino.color = Color.NEGRO;
                    estructura.mete(vecino.vecino);
                }
            }
                
        }
    }

    /**
     * Realiza la acción recibida en cada uno de los vértices de la gráfica, en
     * el orden en que fueron agregados.
     * @param accion la acción a realizar.
     */
    public void paraCadaVertice(AccionVerticeGrafica<T> accion) {
        // Aquí va su código.
        for(Vertice vertice : vertices){
            accion.actua(vertice);
        }


    }

    /**
     * Realiza la acción recibida en todos los vértices de la gráfica, en el
     * orden determinado por BFS, comenzando por el vértice correspondiente al
     * elemento recibido. Al terminar el método, todos los vértices tendrán
     * color {@link Color#NINGUNO}.
     * @param elemento el elemento sobre cuyo vértice queremos comenzar el
     *        recorrido.
     * @param accion la acción a realizar.
     * @throws NoSuchElementException si el elemento no está en la gráfica.
     */
    public void bfs(T elemento, AccionVerticeGrafica<T> accion) {
        // Aquí va su código.
        recorre(elemento, accion, new Cola<Vertice>());
        paraCadaVertice((v) -> setColor(v, Color.NINGUNO));

    }


    /**
     * Realiza la acción recibida en todos los vértices de la gráfica, en el
     * orden determinado por DFS, comenzando por el vértice correspondiente al
     * elemento recibido. Al terminar el método, todos los vértices tendrán
     * color {@link Color#NINGUNO}.
     * @param elemento el elemento sobre cuyo vértice queremos comenzar el
     *        recorrido.
     * @param accion la acción a realizar.
     * @throws NoSuchElementException si el elemento no está en la gráfica.
     */
    public void dfs(T elemento, AccionVerticeGrafica<T> accion) {
        // Aquí va su código.
        recorre(elemento, accion, new Pila<Vertice>());
        paraCadaVertice((v) -> setColor(v, Color.NINGUNO));

    }


    // Metodo que devuelve LA LISTA de componentes conexas de una grafica.
    public List<List<VerticeGrafica<T>>> componentesConexas() {
        List<List<VerticeGrafica<T>>> componentes = new ArrayList<>();
        paraCadaVertice(v -> setColor(v, Color.ROJO));

        for (Vertice vertice : vertices) {
            if (vertice.color == Color.ROJO) {
                List<VerticeGrafica<T>> componente = new ArrayList<>();
                recorre(vertice.elemento, v -> componente.add((VerticeGrafica<T>) v), new Pila<>());
                componentes.add(componente);
            }
        }

        paraCadaVertice(v -> setColor(v, Color.NINGUNO));

        // Por cada componente conexa en la lista de componentes, imprimimos sus elementos (vertices y pesos).
        int contador = 1;
        for (List<VerticeGrafica<T>> componente : componentes) {
            System.out.println("\n");
            System.out.println("Componente conexa " + contador + ": ");
            for (VerticeGrafica<T> vertice : componente) {
                System.out.println("Vertice:" + vertice);
                Vertice v = (Vertice) vertice;
                for (Vecino vecino : v.vecinos) {
                    System.out.println("Vecino: " + vecino.vecino + " Peso: " + vecino.peso);
                }
            }
            contador++;
        }

        return componentes;
    }


        /**
     * Encuentra el árbol de peso mínimo en la componente conexa a la que pertenece el vértice inicial.
     * @param elemento el elemento del vértice inicial.
     * @return una nueva gráfica que representa el árbol de peso mínimo en la componente conexa.
     * @throws NoSuchElementException si el elemento no está en la gráfica.
     */
    public Grafica<T> arbolPesoMinimo(T elemento) {
        if (!contiene(elemento)) {
            throw new NoSuchElementException();
        }

        Vertice verticeInicial = (Vertice) vertice(elemento);
        return arbolPesoMinimoDFS(verticeInicial);
    }

    private Grafica<T> arbolPesoMinimoDFS(Vertice verticeInicial) {
        Grafica<T> arbol = new Grafica<>();
        Cola<Vertice> cola = new Cola<>();
        HashSet<Vertice> visitados = new HashSet<>();

        cola.mete(verticeInicial);

        while (!cola.esVacia()) {
            Vertice actual = cola.saca();
            if (!visitados.contains(actual)) {
                visitados.add(actual);
                arbol.agrega(actual.elemento);

                for (Vecino vecino : actual.vecinos) {
                    cola.mete(vecino.vecino);
                }
            }
        }

        return arbol;
    }


    // A partir de una lista de componentes conexas, obtenemos el arbol de peso minimo para
    // cada componente conexa y lo agregamos a una nueva grafica.
    /**
     * Encuentra el bosque de peso mínimo en la gráfica conexa.
     * @return una nueva gráfica que representa el bosque de peso mínimo.
     */
    public Grafica<T> bosquePesoMinimo() {
        Grafica<T> bosque = new Grafica<>();
        List<List<VerticeGrafica<T>>> componentes = componentesConexas();

        for (List<VerticeGrafica<T>> componente : componentes) {
            Grafica<T> arbol = new Grafica<>();
            for (VerticeGrafica<T> vertice : componente) {
                arbol.agrega(vertice.get());
            }

            for (VerticeGrafica<T> vertice : componente) {
                Vertice v = (Vertice) vertice;
                for (Vecino vecino : v.vecinos) {
                    if (!arbol.sonVecinos(v.elemento, vecino.vecino.elemento)) {
                        arbol.conecta(v.elemento, vecino.vecino.elemento, vecino.peso);
                    }
                }
            }

            bosque = bosque.union(arbol.arbolPesoMinimo(componente.get(0).get()));
        }

        System.out.println(bosque);
        return bosque;

    }


    // Metodo que devuelve la union de dos graficas.

    public Grafica<T> union(Grafica<T> grafica) {
        Grafica<T> union = new Grafica<>();

        for (Vertice vertice : vertices) {
            union.agrega(vertice.elemento);
        }

        for (Vertice vertice : grafica.vertices) {
            union.agrega(vertice.elemento);
        }

        for (Vertice vertice : vertices) {
            for (Vecino vecino : vertice.vecinos) {
                union.conecta(vertice.elemento, vecino.vecino.elemento, vecino.peso);
            }
        }

        for (Vertice vertice : grafica.vertices) {
            for (Vecino vecino : vertice.vecinos) {
                union.conecta(vertice.elemento, vecino.vecino.elemento, vecino.peso);
            }
        }

        return union;
    }




    /**
     * Regresa una gráfica que representa el subgrafo inducido por los elementos
     * contenidos en la gráfica.
     * @param elementos los elementos para los que queremos el subgrafo inducido.
     * @return una gráfica que representa el subgrafo inducido por los elementos
     *         contenidos en la gráfica.
     */

    public Grafica<T> subgrafica(List<T> elementos) {
        // Aquí va su código.
        Grafica<T> subgrafica = new Grafica<>();

        for(T elemento : elementos){
            if(!contiene(elemento)){
                throw new NoSuchElementException();
            }
                
            subgrafica.agrega(elemento);
        }

        for(T elemento : elementos){
            Vertice vertice = (Vertice) vertice(elemento);

            for(Vecino vecino : vertice.vecinos){
                if(subgrafica.contiene(vecino.vecino.elemento)){
                    subgrafica.conecta(elemento, vecino.vecino.elemento, vecino.peso);
                }
            }
                
        }

        return subgrafica;
    }


    

    













    /**
     * Nos dice si la gráfica es vacía.
     * @return <code>true</code> si la gráfica es vacía, <code>false</code> en
     *         otro caso.
     */
    @Override public boolean esVacia() {
        // Aquí va su código.
        return vertices.esVacia();
    }

    /**
     * Limpia la gráfica de vértices y aristas, dejándola vacía.
     */
    @Override public void limpia() {
        // Aquí va su código.
        vertices.limpia();
        aristas = 0;
    }

    /**
     * Regresa una representación en cadena de la gráfica.
     * @return una representación en cadena de la gráfica.
     */
    @Override public String toString() {
        String texto = "{";
    
        for(Vertice vertice : vertices){
            texto += String.format("%s, ", vertice.elemento.toString());
        }
            
        texto += "}, \n  {";
        Lista<T> verticesPasados = new Lista<>();
    
        for(Vertice vertice : vertices){
            for(Vecino vecino : vertice.vecinos){
                if(!verticesPasados.contiene(vecino.vecino.elemento)){
                    texto += String.format("(%s, %s, %s), ", vertice.elemento.toString(), vecino.vecino.elemento.toString(), vecino.peso);
                }
            }
    
            verticesPasados.agrega(vertice.elemento);
    
        }
    
        texto += "}";
        return texto;
    }

    /**
     * Nos dice si la gráfica es igual al objeto recibido.
     * @param objeto el objeto con el que hay que comparar.
     * @return <code>true</code> si la gráfica es igual al objeto recibido;
     *         <code>false</code> en otro caso.
     */
    @Override public boolean equals(Object objeto) {
        if (objeto == null || getClass() != objeto.getClass())
            return false;
        @SuppressWarnings("unchecked") Grafica<T> grafica = (Grafica<T>)objeto;
        // Aquí va su código.
        if(aristas != grafica.aristas || vertices.getElementos() != grafica.vertices.getElementos()){
            return false;
        }
            
        for(Vertice vertice : vertices){

            if (!grafica.contiene(vertice.elemento)){
                return false;
            }
                
            Vertice vertice2 = (Vertice) grafica.vertice(vertice.elemento);

            if(vertice.vecinos.getElementos() != vertice2.vecinos.getElementos()){
                return false;
            }

            for(Vecino vecino1 : vertice.vecinos){
                boolean contiene = false;

                for(Vecino vecino2 : vertice2.vecinos){
                    if(vecino1.vecino.elemento.equals(vecino2.vecino.elemento)){
                        contiene = true;
                        break;
                    }
                }

                if(!contiene){
                    return false;
                }
                    
            }

        }

        return true;
        
    }

    /**
     * Regresa un iterador para iterar la gráfica. La gráfica se itera en el
     * orden en que fueron agregados sus elementos.
     * @return un iterador para iterar la gráfica.
     */
    @Override public Iterator<T> iterator() {
        return new Iterador();
    }

    /**
     * Calcula una trayectoria de distancia mínima entre dos vértices.
     * @param origen el vértice de origen.
     * @param destino el vértice de destino.
     * @return Una lista con vértices de la gráfica, tal que forman una
     *         trayectoria de distancia mínima entre los vértices <code>a</code> y
     *         <code>b</code>. Si los elementos se encuentran en componentes conexos
     *         distintos, el algoritmo regresa una lista vacía.
     * @throws NoSuchElementException si alguno de los dos elementos no está en
     *         la gráfica.
     */
    public Lista<VerticeGrafica<T>> trayectoriaMinima(T origen, T destino) {
        // Aquí va su código.
        if(!contiene(origen) || !contiene(destino)){
            throw new NoSuchElementException();
        }

        Vertice vertice = (Vertice) vertice(origen);

        if(origen.equals(destino)){
            Lista<VerticeGrafica<T>> lista = new Lista<>();
            lista.agrega(vertice);
            return lista;
        }

        for(Vertice v : vertices){
            v.distancia = Double.MAX_VALUE;
        }

        vertice.distancia = 0;

        Cola<Vertice> cola = new Cola<>();
        cola.mete(vertice);

        while(!cola.esVacia()){
            vertice = cola.saca();

            for(Vecino vecino : vertice.vecinos){
                if(vecino.vecino.distancia == Double.MAX_VALUE){
                    vecino.vecino.distancia = vertice.distancia + 1;
                    cola.mete(vecino.vecino);
                }
            }
                
        }

        return caminoDeRegreso((aux, vecino) -> vecino.vecino.distancia == aux.distancia - 1, (Vertice) vertice(destino));
    
    }

    @SuppressWarnings("unchecked")
    private Lista<VerticeGrafica<T>> caminoDeRegreso(BuscadorCamino buscador, Vertice destino) {
        
        Vertice verticeAux = destino;
        Lista<VerticeGrafica<T>> trayectoria = new Lista<>();

        if(verticeAux.distancia == Double.MAX_VALUE){
            return new Lista<VerticeGrafica<T>>();
        }

        trayectoria.agrega(verticeAux);
        
        while(verticeAux.distancia != 0){
            for(Vecino vecino : verticeAux.vecinos){
                if(buscador.seSiguen(verticeAux, vecino)){
                    trayectoria.agrega(vecino.vecino);
                    verticeAux = vecino.vecino;
                    break;
                }

            }
        }

        return trayectoria.reversa();

    }

    /**
     * Calcula la ruta de peso mínimo entre el elemento de origen y el elemento
     * de destino.
     * @param origen el vértice origen.
     * @param destino el vértice destino.
     * @return una trayectoria de peso mínimo entre el vértice <code>origen</code> y
     *         el vértice <code>destino</code>. Si los vértices están en componentes
     *         conexas distintas, regresa una lista vacía.
     * @throws NoSuchElementException si alguno de los dos elementos no está en
     *         la gráfica.
     */
    public Lista<VerticeGrafica<T>> dijkstra(T origen, T destino) {
        // Aquí va su código.
        if(!contiene(origen) || !contiene(destino)){
            throw new NoSuchElementException();
        }

        for(Vertice vertice : vertices){
            vertice.distancia = Double.MAX_VALUE;
        }

        Vertice verticeOrigen = (Vertice) vertice(origen);
        verticeOrigen.distancia = 0;

        MonticuloDijkstra<Vertice> monticulo;
        int n = vertices.getElementos();

        if(aristas > ((n*(n - 1))/2)-n){
            monticulo = new MonticuloArreglo<>(vertices, vertices.getElementos());
        }else{
            monticulo = new MonticuloMinimo<>(vertices, vertices.getElementos());
        }
            

        while(!monticulo.esVacia()){
            Vertice raiz = monticulo.elimina();

            for(Vecino vecino : raiz.vecinos){
                if(vecino.vecino.distancia > raiz.distancia + vecino.peso){
                    vecino.vecino.distancia = raiz.distancia + vecino.peso;
                    monticulo.reordena(vecino.vecino);
                }
            }
                
        }

        return caminoDeRegreso((vertice, vecino) -> vecino.vecino.distancia + vecino.peso == vertice.distancia, (Vertice) vertice(destino));
        
    }

    /**
     * Metodo que agrega una arista a la gráfica.
     * @param apply  El primer elemento de la arista.
     * @param apply2  El segundo elemento de la arista.
     * @param string  El peso de la arista.
     */
    public void agrega(T apply, T apply2, String string) {
        // Aquí va su código.
        if(apply == null || apply2 == null){
            throw new IllegalArgumentException();
        }

        if(!contiene(apply)){
            agrega(apply);
        }

        if(!contiene(apply2)){
            agrega(apply2);
        }

        Vertice verticePrimero = (Vertice) vertice(apply);
        Vertice verticeSegundo = (Vertice) vertice(apply2);

        if(sonVecinos(verticePrimero.elemento, verticeSegundo.elemento)){
            throw new IllegalArgumentException();
        }

        int peso = Integer.parseInt(string);

        verticePrimero.vecinos.agrega(apply2, (new Vecino(verticeSegundo, peso)));
        verticeSegundo.vecinos.agrega(apply, (new Vecino(verticePrimero, peso)));

        aristas++;

    }

    public Iterator<T> vertices() {
        return new Iterador();
    }

    public boolean sonAdyacentes(T vertice, T verticeActual) {
        Vertice verticePrimero = (Vertice) vertice(vertice);
        Vertice verticeSegundo = (Vertice) vertice(verticeActual);

        return verticePrimero.vecinos.contiene(verticeActual) && verticeSegundo.vecinos.contiene(vertice);
        
    }

    public int indiceDe(T vertice) {
        Vertice verticeAux = (Vertice) vertice(vertice);
        return verticeAux.indice;
    }

    public T[] vecinos(T vertice) {
        Vertice verticeAux = (Vertice) vertice(vertice);
        T[] vecinos = (T[]) new Object[verticeAux.vecinos.getElementos()];

        int i = 0;
        for(Vecino vecino : verticeAux.vecinos){
            vecinos[i] = vecino.vecino.elemento;
            i++;
        }

        return vecinos;
        
    }

    public int grado(T vertice) {
        Vertice verticeAux = (Vertice) vertice(vertice);
        return verticeAux.vecinos.getElementos();
    }



    

    public int getIndice(T vertice) {
        Vertice verticeAux = (Vertice) vertice(vertice);
        return verticeAux.indice;
    }

    public void setIndice(T vertice, int indice) {
        Vertice verticeAux = (Vertice) vertice(vertice);
        verticeAux.indice = indice;
    }

    public void setVecino(T vertice, T vecino, double peso) {
        Vertice verticePrimero = (Vertice) vertice(vertice);
        Vertice verticeSegundo = (Vertice) vertice(vecino);

        if(!sonVecinos(verticePrimero.elemento, verticeSegundo.elemento)){
            throw new IllegalArgumentException();
        }
            

        for(Vecino vecino1 : verticePrimero.vecinos){
            if(vecino1.vecino.equals(verticeSegundo)){
                vecino1.peso = peso;
                break;
            }
        }
            

        for(Vecino vecino1 : verticeSegundo.vecinos){
            if(vecino1.vecino.equals(verticePrimero)){
                vecino1.peso = peso;
                break;
            }
        }
            
    }

    public void eliminaVecino(T vertice, T vecino) {
        Vertice verticePrimero = (Vertice) vertice(vertice);
        Vertice verticeSegundo = (Vertice) vertice(vecino);

        if(!sonVecinos(verticePrimero.elemento, verticeSegundo.elemento)){
            throw new IllegalArgumentException();
        }
            

        verticePrimero.vecinos.elimina(vecino);
        verticeSegundo.vecinos.elimina(vertice);
    }





    





    
}
