import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;

import visual.*;
import adoquinamiento.*;

public class Main {

    public static void main(String[] args) throws IOException {
        int k = Integer.parseInt(args[0]);
        int m = (int) Math.pow(2, k);

        // Crear la cuadricula
        Cuadricula cuadricula = new Cuadricula(m, m);

        // Verificar el tamaño de la cuadricula
        if (cuadricula.getM() == m && cuadricula.getN() == m) {
            // Colocar el cuadrado especial
            cuadricula.colocarCuadradoEspecial(new Cuadrado(0, 0, 0));

            // Llenar la cuadricula con adoquines
            cuadricula.adoquinar();

            // Generar el GIF
            int numFrames = m * m;
            BufferedImage[] frames = new BufferedImage[numFrames];
            for (int i = 0; i < numFrames; i++) {
                frames[i] = cuadricula.obtenerImagen(i);
            }

            // Guardar el GIF
            AnimatedGifEncoder encoder = new AnimatedGifEncoder();
            encoder.setRepeat(0);
            encoder.setFrameRate(10);
            encoder.setDelay(100);
            encoder.start("cuadricula.gif");
            for (BufferedImage frame : frames) {
                encoder.addFrame(frame);
            }
            encoder.finish();
        } else {
            System.err.println("Error: La cuadricula no tiene el tamaño correcto");
            System.exit(1);
        }
    }

}