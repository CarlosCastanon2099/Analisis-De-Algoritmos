import clases.*;

/*  
 * AdaptadorArista.java
 */

public class AdaptadorArista<T> {
    private T vertice1;
    private T vertice2;
    private int peso;

    public AdaptadorArista(T vertice1, T vertice2, int peso) {
        this.vertice1 = vertice1;
        this.vertice2 = vertice2;
        this.peso = peso;
    }

    public T getVertice1() {
        return vertice1;
    }

    public T getVertice2() {
        return vertice2;
    }

    public int getPeso() {
        return peso;
    }

    public String toString() {
        return "(" + vertice1 + ", " + vertice2 + ", " + peso + ")";
    }

}
