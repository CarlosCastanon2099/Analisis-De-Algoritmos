import adoquinamiento.*;

public class Main {

    public static void main(String[] args) {
        int k = Integer.parseInt(args[0]);
        int m = (int) Math.pow(2, k);

        // Crear la cuadricula
        Cuadricula cuadricula = new Cuadricula(m, m);

        // Verificar el tamaño de la cuadricula
        if (cuadricula.getM() == m && cuadricula.getN() == m) {

            // Llenar la cuadricula con adoquines
            cuadricula.adoquinar();

            // Imprimir la cuadricula en la terminal
            imprimirCuadricula(cuadricula);
        } else {
            System.err.println("Error: La cuadricula no tiene el tamaño correcto");
            System.exit(1);
        }
    }

    // Metodo para imprimir la cuadricula en la terminal
    // en caso de que un cuadrito pertenezca a un mismo polinomio, lo denotaremos como
    // un numero entero, en caso contrario lo denotaremos como un 0
    // para el cuadrado especial tendremos el numero 9

    public static void imprimirCuadricula(Cuadricula cuadricula) {
        int m = cuadricula.getM();
        int n = cuadricula.getN();
        Cuadrado[][] cuadriculaArreglo = cuadricula.getCuadricula();
        for (int i = 0; i < m; i++) {
            System.out.print("|");
            for (int j = 0; j < n; j++) {
                if (cuadriculaArreglo[i][j] == null) {
                    System.out.print("00|");
                } else {
                    System.out.print(cuadriculaArreglo[i][j].getColor() + "|");
                }
            }
            System.out.println();
        }
    }


}