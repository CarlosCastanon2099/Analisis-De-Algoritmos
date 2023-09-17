package adoquinamiento;

// Clase que hereda de Adoquin para poder formar
/** 
 * 2) ⅃ 
 * |----|----|
 * |    | *  |
 * |----|----|
 * | *  | *  |
 * |----|----|
 */
public class AdoquinDos extends Adoquin {
    Cuadrado cuadrito1;
    Cuadrado cuadrito2;
    Cuadrado cuadrito3;
    
    int x;
    int y;
    int color;

    // Constructor de la clase
    public AdoquinDos(Cuadrado cuadrito1, Cuadrado cuadrito2, Cuadrado cuadrito3) {
        super(cuadrito1, cuadrito2, cuadrito3);
        cuadrito1 = new Cuadrado(x, y, color);
        cuadrito2 = new Cuadrado(x - 1, y, color);
        cuadrito3 = new Cuadrado(x, y + 1, color);
    }
}
