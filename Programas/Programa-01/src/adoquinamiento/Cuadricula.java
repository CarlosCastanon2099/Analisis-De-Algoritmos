package adoquinamiento;

//import java.util.Random;

public class Cuadricula {
    // Clase en la que declaramos la cuadricula 
    // La cuadricula debe ser de m * m
    // Con m = 2^k es decir m debe ser potencia de 2.
    // Si bien a la cuadricula la componen cuadrados
    // Esta solo puede ser rellenada por adoquines y un solo cuadrado especial

    // Atributos de la clase
    private int size;
    private int[][] cuadricula;

    // Constructor de la clase
    public Cuadricula(int size) {
        this.size = size;
        this.cuadricula = new int[size][size];
    }

    // Metodos de la clase
    // Metodo para obtener el tamaño de la cuadricula
    public int getSize() {
        return size;
    }

    // Metodo para obtener la cuadricula
    public int[][] getCuadricula() {
        return cuadricula;
    }

    // Metodo para cambiar el tamaño de la cuadricula
    public void setSize(int size) {
        this.size = size;
    }

    // Metodo para cambiar la cuadricula
    public void setCuadricula(int[][] cuadricula) {
        this.cuadricula = cuadricula;
    }


    
    
}