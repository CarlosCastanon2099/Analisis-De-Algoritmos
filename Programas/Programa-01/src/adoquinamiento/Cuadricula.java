package adoquinamiento;

import java.awt.image.BufferedImage;
import java.util.Random;

public class Cuadricula {

    // Atributos de la clase
    private int m;
    private int n;
    private Cuadrado[][] cuadricula;
    private Cuadrado cuadradoEspecial;

    // Constructor de la clase
    public Cuadricula(int m, int n) {
        this.m = m;
        this.n = n;
        this.cuadricula = new Cuadrado[m][n];
        this.cuadradoEspecial = null;
    }

    // Métodos de la clase

    // Metodo para obtener el tamaño de la cuadricula en x
    public int getM() {
        return m;
    }

    // Metodo para obtener el tamaño de la cuadricula en y
    public int getN() {
        return n;
    }

    // Metodo para obtener la celda en la posicion x,y
    public Cuadrado getCelda(int x, int y) {
        return cuadricula[x][y];
    }

    // Metodo para colocar el cuadrado especial en la cuadricula
    public void colocarCuadradoEspecial(Cuadrado cuadradoEspecial) {
        this.cuadradoEspecial = cuadradoEspecial;
    }

    // Metodo para colocar una figura L en la cuadricula en la posicion x,y
    public void colocarAdoquinUno(Adoquin adoquin, int x, int y) {
        cuadricula[x][y] = adoquin.getCuadrito1();
        cuadricula[x][y+1] = adoquin.getCuadrito2();
        cuadricula[x+1][y] = adoquin.getCuadrito3();
    }

    // Metodo para colocar una figura L en la cuadricula en la posicion x,y
    public void colocarAdoquinDos(Adoquin adoquin, int x, int y) {
        cuadricula[x][y] = adoquin.getCuadrito1();
        cuadricula[x-1][y] = adoquin.getCuadrito2();
        cuadricula[x][y+1] = adoquin.getCuadrito3();
    }

    // Metodo para colocar una figura L en la cuadricula en la posicion x,y
    public void colocarAdoquinTres(Adoquin adoquin, int x, int y) {
        cuadricula[x][y] = adoquin.getCuadrito1();
        cuadricula[x][y-1] = adoquin.getCuadrito2();
        cuadricula[x-1][y] = adoquin.getCuadrito3();
    }

    // Metodo para colocar una figura L en la cuadricula en la posicion x,y
    public void colocarAdoquinCuatro(Adoquin adoquin, int x, int y) {
        cuadricula[x][y] = adoquin.getCuadrito1();
        cuadricula[x+1][y] = adoquin.getCuadrito2();
        cuadricula[x][y-1] = adoquin.getCuadrito3();
    }

    // Metodo que nos dice si hay algun cuadrado vacio
    // en las posiciones aledañas a la entrada x,y
    // regresa la o las posicion(es) que no contengan algun cuadrado
    public int[] hayCuadradoVacio(int x, int y) {
        int[] posicion = new int[2];
        posicion[0] = -1;
        posicion[1] = -1;
        if (x + 1 < m && cuadricula[x + 1][y] == null) {
            posicion[0] = x + 1;
            posicion[1] = y;
        } else if (x - 1 >= 0 && cuadricula[x - 1][y] == null) {
            posicion[0] = x - 1;
            posicion[1] = y;
        } else if (y + 1 < n && cuadricula[x][y + 1] == null) {
            posicion[0] = x;
            posicion[1] = y + 1;
        } else if (y - 1 >= 0 && cuadricula[x][y - 1] == null) {
            posicion[0] = x;
            posicion[1] = y - 1;
        }
        return posicion;
    }

    // Metodo que nos dice si hay espacio para colocar alguno
    // de los cuatro adoquines a partir de una posicion x,y
    // regresa la posicion disponible mas proxima a algun adoquin o cuadrado
    public int[] hayEspacio(int x, int y) {
        int[] posicion = new int[2];
        posicion[0] = -1;
        posicion[1] = -1;
        if (x + 1 < m && cuadricula[x + 1][y] == null) {
            posicion[0] = x + 1;
            posicion[1] = y;
        } else if (x - 1 >= 0 && cuadricula[x - 1][y] == null) {
            posicion[0] = x - 1;
            posicion[1] = y;
        } else if (y + 1 < n && cuadricula[x][y + 1] == null) {
            posicion[0] = x;
            posicion[1] = y + 1;
        } else if (y - 1 >= 0 && cuadricula[x][y - 1] == null) {
            posicion[0] = x;
            posicion[1] = y - 1;
        }
        return posicion;
    }


    // Metodo que hace la verificacion si se puede poner un adoquin partiendo de
    // una base x,y, el metodo verifica si no hay algun otro cuadro/adoquin
    // que impida la colocacion del nuevo adoquin, si no los hay lo pone



    // Algoritmo de adoquinamiento
    public void adoquinar() {
        // Colocar el cuadrado especial
        colocarCuadradoEspecial(new Cuadrado(0, 0, 0));
    
        // Colocar las figuras L
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (cuadricula[i][j] == null) {
                    // Elegir un color aleatorio
                    int color = (int) Math.random() * 255;
    
                    // Colocar el cuadrado especial
                    colocarCuadradoEspecial(new Cuadrado(i, j, color));
                    
                }
                
                // Caso 1) L 
                if (cuadricula[i][j] == null && cuadricula[i][j+1] == null && cuadricula[i+1][j] == null) {
                    // Elegir un color aleatorio
                    int color = (int) Math.random() * 255;
                    Cuadrado cuadrito1 = new Cuadrado(i, j, color);
                    Cuadrado cuadrito2 = new Cuadrado(i, j+1, color);
                    Cuadrado cuadrito3 = new Cuadrado(i+1, j, color);

                    AdoquinUno adoquin = new AdoquinUno(cuadrito1, cuadrito2, cuadrito3);

                    colocarAdoquinUno(adoquin, i, j);
    
                }

                // Caso 2) ⅃
                if (cuadricula[i][j] == null && cuadricula[i-1][j] == null && cuadricula[i][j+1] == null) {
                    // Elegir un color aleatorio
                    int color = (int) Math.random() * 255;
                    Cuadrado cuadrito1 = new Cuadrado(i, j, color);
                    Cuadrado cuadrito2 = new Cuadrado(i-1, j, color);
                    Cuadrado cuadrito3 = new Cuadrado(i, j+1, color);

                    AdoquinDos adoquin = new AdoquinDos(cuadrito1, cuadrito2, cuadrito3);

                    colocarAdoquinDos(adoquin, i, j);
    
                }
                
                // Caso 3) ꓶ
                if (cuadricula[i][j] == null && cuadricula[i][j-1] == null && cuadricula[i-1][j] == null) {
                    // Elegir un color aleatorio
                    int color = (int) Math.random() * 255;
                    Cuadrado cuadrito1 = new Cuadrado(i, j, color);
                    Cuadrado cuadrito2 = new Cuadrado(i, j-1, color);
                    Cuadrado cuadrito3 = new Cuadrado(i-1, j, color);

                    AdoquinTres adoquin = new AdoquinTres(cuadrito1, cuadrito2, cuadrito3);

                    colocarAdoquinTres(adoquin, i, j);
    
                }

                // Caso 4) Γ
                if (cuadricula[i][j] == null && cuadricula[i+1][j] == null && cuadricula[i][j-1] == null) {
                    // Elegir un color aleatorio
                    int color = (int) Math.random() * 255;
                    Cuadrado cuadrito1 = new Cuadrado(i, j, color);
                    Cuadrado cuadrito2 = new Cuadrado(i+1, j, color);
                    Cuadrado cuadrito3 = new Cuadrado(i, j-1, color);

                    AdoquinCuatro adoquin = new AdoquinCuatro(cuadrito1, cuadrito2, cuadrito3);

                    colocarAdoquinCuatro(adoquin, i, j);
    
                }



                    
                


            }
        }
    }



    // Metodo para obtener la imagen de la cuadricula en un momento dado
    public BufferedImage obtenerImagen(int i) {
        BufferedImage imagen = new BufferedImage(m, n, BufferedImage.TYPE_INT_RGB);
        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                imagen.setRGB(x, y, cuadricula[x][y].getColor());
            }
        }
        return imagen;
    }



}