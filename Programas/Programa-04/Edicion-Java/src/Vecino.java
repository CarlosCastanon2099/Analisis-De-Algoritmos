
public class Vecino<T> {
    private T vertice;
    private int peso;

    public Vecino(T vertice, int peso) {
        this.vertice = vertice;
        this.peso = peso;
    }

    public T get() {
        return vertice;
    }

    public int getPeso() {
        return peso;
    }

    public String toString() {
        return "(" + vertice + ", " + peso + ")";
    }

}
