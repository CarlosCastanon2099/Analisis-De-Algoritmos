package adoquinamiento;

// Clase especializada en Adoquines
// Aqui se encuentra el objeto adoquin el cual tiene forma de L
// Aqui tambien diremos que es un adoquin y que no lo es
// A una L le corresponden 3 cuadros, esta puede estar en cualquier posicion
// de la cuadricula y una de las formas en las que puede lucir es esta 
/*
 * 
 * forma de “L”, como el siguiente:

|----|----|
| *  |    |
|----|----|
| *  | *  |
|----|----|

 */


public class Adoquin {

    // Constructor de la clase Adoquin
    // Un adoquin esta formado por tres cuadritos
    // Cada uno de los cuadritos que forman a un adoquin deben de tener el mismo color
    // y tener minimo una conexion con otro cuadrito que conforme al adoquin en el que esta
    // Cada adoquin debe tener forzozamente forma de L incluyendo todas sus variantes como
    // L volteada, invertida, volteada e invertida

    // Atributos de la clase
    private Cuadrado cuadrito1;
    private Cuadrado cuadrito2;
    private Cuadrado cuadrito3;

    // Constructor de la clase
    public Adoquin(Cuadrado cuadrito1, Cuadrado cuadrito2, Cuadrado cuadrito3) {
        this.cuadrito1 = cuadrito1;
        this.cuadrito2 = cuadrito2;
        this.cuadrito3 = cuadrito3;
    }

    // Metodos de la clase
    // Metodo para obtener el primer cuadrito de un adoquin
    public Cuadrado getCuadrito1() {
        return cuadrito1;
    }

    // Metodo para obtener el segundo cuadrito de un adoquin
    public Cuadrado getCuadrito2() {
        return cuadrito2;
    }

    // Metodo para obtener el tercer cuadrito de un adoquin
    public Cuadrado getCuadrito3() {
        return cuadrito3;
    }

    // Metodo para cambiar el primer cuadrito de un adoquin
    public void setCuadrito1(Cuadrado cuadrito1) {
        this.cuadrito1 = cuadrito1;
    }

    // Metodo para cambiar el segundo cuadrito de un adoquin
    public void setCuadrito2(Cuadrado cuadrito2) {
        this.cuadrito2 = cuadrito2;
    }

    // Metodo para cambiar el tercer cuadrito de un adoquin
    public void setCuadrito3(Cuadrado cuadrito3) {
        this.cuadrito3 = cuadrito3;
    }


}
