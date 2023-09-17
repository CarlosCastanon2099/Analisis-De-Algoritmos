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

}
