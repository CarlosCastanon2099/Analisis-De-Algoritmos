
import clases.*;
import clases.Grafica.Vertice;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;
import java.util.function.Function;
import java.text.NumberFormat;


/**
 * Programa 4
 */
public class Programa4 {

    /**
     * Método principal
     * @param args Argumentos de la línea de comandos
     * @throws IOException Si ocurre un error al leer el archivo de texto
     * @throws NoSuchElementException Si ocurre un error al leer el archivo de texto
     * @throws NumberFormatException Si ocurre un error al leer el archivo de texto
     * @throws ArrayIndexOutOfBoundsException Si ocurre un error al leer el archivo de texto
     */
    public static void main(String[] args) throws IOException, NoSuchElementException, NumberFormatException, ArrayIndexOutOfBoundsException {
        /*
        * Sea G una gráfica disconexa con n vértices y e aristas, 
        * utilizamos DFS para determinar el bosque generador de peso mínimo de la grafica G disconexa.

        * Queremos realizar un programa el cual reciba como entrada en los argumentos de la
        * línea de comandos (ejecutando desde la carpeta ’src’) un archivo de texto
        * tal que:
        * - En la primera línea tendrá todos los vértices que forman a G,
        * separados por una coma (’,’).
        * - En las siguientes líneas irán pares de vértices, separados por una
        * coma (’,’), que indicará en las aristas de G, seguido de dos puntos
        * (‘ : ’) para indicar el peso de la arista.
* 
        * Un ejemplo de archivo de entrada es el siguiente:
        * 1,2,3,4,5,6,7,8
        * 1,2:1
        * 5,6:3
        * 7,8:4
        * 4,3:5
        * 6,1:4
        * 6,7:1
        * 3,8:3
        * 5,4:2
        * 4,2:9
        * 3,7:1
        * 2,6:3
        * 7,5:5
        * 8,4:1
* 
        * La salida es por línea de comandos y debe de imprimir los
        * vértices y aristas pertenecientes a cada uno de los árboles, de forma similar
        * en que se presentaron las aristas en la entrada (listadas una arista por
        * renglón) diferenciando esta vez entre un árbol y otro.
         */
        
        // El uso del programa es: java Programa4 archivo.txt
        if (args.length != 1) {
            System.out.println("El uso del programa es: java Programa4 archivo.txt");
            return;
        }
        
        

        /* Leemos el archivo de entrada recibido */
        String texto = leerArchivo(args[0]);

        /* Creamos la grafica con la informacion del archivo */
        Grafica<Integer> grafica = crearGrafica(texto, Integer::parseInt);

        /* Imprimimos la grafica */
        System.out.println("Grafica: ");
        System.out.println(grafica);

        /* Preguntamos si la grafica recibida es conexa con el metodo esConexa */
        System.out.println("La grafica es conexa: " + grafica.esConexa());

        /* Si la grafica no es conexa (es disconexa) entonces mostramos sus componentes conexas  */
        if (!grafica.esConexa()) {
            System.out.println("\n");
            System.out.println("Componentes conexas: ");
            grafica.componentesConexas();
            
        }

        /* Si la grafica es disconexa entonces mostramos su bosque generador de peso minimo */
        if (!grafica.esConexa()) {
            System.out.println("\n");
            System.out.println("Bosque generador de peso minimo: ");
            grafica.bosquePesoMinimo();
        }
        
        
       

        
        
        
    }

    // Metodo para leer el archivo que nos pasan como argumento
    private static String leerArchivo(String archivo) throws IOException {
        String cadena;
        String texto = "";
        FileReader f = new FileReader(archivo);
        BufferedReader b = new BufferedReader(f);
        while((cadena = b.readLine()) != null) {
            texto += cadena + "\n";
        }
        b.close();
        return texto;
    }

    /*  
     * Recordando que la estructura de la grafica del archivo es:
     * 1,2,3,4,5,6,7,8
     * 1,2:1
     * 5,6:3
     * 7,8:4
     * 4,3:5
     * 6,1:4
     * 6,7:1
     * 3,8:3
     * 5,4:2
     * 4,2:9
     * 3,7:1
     * 2,6:3
     * 7,5:5
     * 8,4:1
     * 
     *  - En la primera línea tendrá todos los vértices que forman a G,
     * separados por una coma (’,’).
     * - En las siguientes líneas irán pares de vértices, separados por una
     * coma (’,’), que indicará en las aristas de G, seguido de dos puntos
     * (‘ : ’) para indicar el peso de la arista.

     * Procedemos a crear una grafica con esa informacion
     * Usando la clase Grafica.java de nuestra carpeta clases
     */

    private static <T> Grafica<T> crearGrafica(String texto, Function<String, T> convertidor) {
        String[] lineas = texto.split("\n");
        String[] vertices = lineas[0].split(",");
        Grafica<T> grafica = new Grafica<T>();
        for (String vertice : vertices) {
            grafica.agrega(convertidor.apply(vertice));
        }
        for (int i = 1; i < lineas.length; i++) {
            String[] arista = lineas[i].split(":");
            String[] verticesArista = arista[0].split(",");
            grafica.agrega(convertidor.apply(verticesArista[0]), convertidor.apply(verticesArista[1]), arista[1]);
        }
        

        return grafica;
    }











    

    





}
