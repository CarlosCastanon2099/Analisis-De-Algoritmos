package adoquinamiento;

import java.awt.image.BufferedImage;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.awt.Color;

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
    public void colocarCuadradoEspecial(Cuadrado cuadradoEspecial, int x, int y) {
        this.cuadradoEspecial = cuadradoEspecial;
        cuadricula[x][y] = cuadradoEspecial;
    }

    // Metodo para obtener la cuadricula 
    public Cuadrado[][] getCuadricula() {
        return cuadricula;
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



    // Algoritmo de adoquinamiento
    public void adoquinar() {
        // Colocar el cuadrado especial
        int specialX = (int) (Math.random() * m);
        int specialY = (int) (Math.random() * n);
        int specialColor = (int) (Math.random() * 90);
        Cuadrado cuadradoEspecial = new Cuadrado(specialX, specialY, specialColor);
        colocarCuadradoEspecial(cuadradoEspecial, specialX, specialY);
    
        int adoquinType = 0;

        // Caso Base
        // Colocar el primer adoquín de tal manera que cubra el cuadrado especial
        Adoquin cuadradoEspecialAdoquin = new AdoquinUno(null, null, null);
        
        
    
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Saltar el espacio ocupado por el cuadrado especial
                if (i == specialX && j == specialY) {
                    continue;
                }

                if (puedeColocarAdoquin(specialX, adoquinType)){
                    Cuadrado cuadrito1 = new Cuadrado(i, j, adoquinType);
                    Cuadrado cuadrito2 = new Cuadrado(i, j , adoquinType);
                    Cuadrado cuadrito3 = new Cuadrado(i, j, adoquinType);
        
                    switch (adoquinType) {
                        case 0:

                            AdoquinUno adoquinUno = new AdoquinUno(cuadrito1, cuadrito2, cuadrito3);
                            colocarAdoquinUno(adoquinUno, i, j);
                            break;
                        case 1:
                            AdoquinDos adoquinDos = new AdoquinDos(cuadrito1, cuadrito2, cuadrito3);
                            colocarAdoquinDos(adoquinDos, i, j);
                            break;
                        case 2:
                            AdoquinTres adoquinTres = new AdoquinTres(cuadrito1, cuadrito2, cuadrito3);
                            colocarAdoquinTres(adoquinTres, i, j);
                            break;
                        case 3:
                            AdoquinCuatro adoquinCuatro = new AdoquinCuatro(cuadrito1, cuadrito2, cuadrito3);
                            colocarAdoquinCuatro(adoquinCuatro, i, j);
                            break;
                    }
        
                    adoquinType = (adoquinType + 1) % 4; // Cambiar al siguiente tipo de adoquín
                }
    

            }
        }
    }

    // Método para verificar si se puede colocar un adoquín en una posición
    private boolean puedeColocarAdoquin(int x, int y) {
        // Verificar si la posición es válida en la cuadrícula
        if (x >= 0 && x < m - 1 && y >= 0 && y < n - 1) {
            // Verificar si no hay otros cuadrados o adoquines en estas posiciones
            if (cuadricula[x][y] == null && cuadricula[x][y + 1] == null && cuadricula[x + 1][y] == null) {
                return true;
            }
        }
        return false;
    }

    

    // Metodo para obtener la imagen de la cuadricula en un momento dado
    public BufferedImage obtenerImagen(int i) {
        BufferedImage imagen = new BufferedImage(m, n, BufferedImage.TYPE_INT_RGB);

        // Colores
        Color colorCuadradoEspecial = Color.RED; // Color para el cuadrado especial
        Color[] coloresAdoquines = {Color.BLUE, Color.GREEN, Color.ORANGE, Color.YELLOW}; // Colores para los adoquines
        Adoquin[] adoquines = {new AdoquinUno(null, null, null), new AdoquinDos(null, null, null), new AdoquinTres(null, null, null), new AdoquinCuatro(null, null, null)};

        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                int color;
                if (cuadricula[x][y] == null) {
                    color = Color.WHITE.getRGB(); // Color de fondo si no hay cuadrado
                } else if (cuadricula[x][y] == cuadradoEspecial) {
                    color = colorCuadradoEspecial.getRGB(); // Color del cuadrado especial
                } else {
                    int adoquinIndex = Arrays.asList(adoquines).indexOf(cuadricula[x][y]);
                    color = coloresAdoquines[adoquinIndex].getRGB(); // Color de los adoquines
                }
                imagen.setRGB(x, y, color);
            }
        }
        return imagen;
    }



}