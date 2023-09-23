package adoquinamiento;

public class Cuadrado {
    // Clase para declarar a los cuadritos de la cuadricula 
    // Esta clase es la que se va a usar para hacer la cuadricula

    // Atributos de la clase
    private int x;
    private int y;
    private int color;

    // Constructor de la clase
    public Cuadrado(int x, int y, int color) {
        this.x = x;
        this.y = y;
        this.color = color;
    }

    // Metodos de la clase
    // Metodo para obtener la posicion en x de un cuadrito
    public int getX() {
        return x;
    }

    // Metodo para obtener la posicion en y de un cuadrito
    public int getY() {
        return y;
    }

    // Metodo para obtener el color de un cuadrito
    public int getColor() {
        return color;
    }

    // Metodo para cambiar el color de un cuadrito
    public void setColor(int color) {
        this.color = color;
    }

    // Metodo para cambiar la posicion en x de un cuadrito
    public void setX(int x) {
        this.x = x;
    }

    // Metodo para cambiar la posicion en y de un cuadrito
    public void setY(int y) {
        this.y = y;
    }

    //Metodo que a partir de una posicion x,y genera un cuadrado 
    public Cuadrado generarCuadrado(int x, int y) {
        Cuadrado cuadrito = new Cuadrado(x, y, 0);
        return cuadrito;
    }

    // Metodo que genera un cuadrado a partir de un arreglo [x,y]
    public Cuadrado generarCuadradoArreglo(int[] posicion) {
        Cuadrado cuadrito = new Cuadrado(posicion[0], posicion[1], 0);
        return cuadrito;
    }

    // Metodo para recuperar un cuadrado
    public Cuadrado getCuadrado(Cuadrado cuadrito) {
        return cuadrito;
    }


}
