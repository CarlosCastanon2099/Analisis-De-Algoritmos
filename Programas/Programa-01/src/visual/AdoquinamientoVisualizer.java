package visual;

import javax.swing.*;

import adoquinamiento.Cuadricula;

import java.awt.*;
import java.awt.image.BufferedImage;

public class AdoquinamientoVisualizer extends JPanel {
    private BufferedImage image;
    private Cuadricula cuadricula;

    // Inicializa la cuadrícula y la imagen
    public AdoquinamientoVisualizer(Cuadricula cuadricula) {
        this.cuadricula = cuadricula;
        this.image = new BufferedImage(cuadricula.getSize(), cuadricula.getSize(), BufferedImage.TYPE_INT_RGB);
        // Configura la ventana y otros componentes de Swing o JavaFX
        

        // Inicia el proceso de adoquinamiento y actualiza la imagen paso a paso
        

        // Genera el GIF con los pasos intermedios
        
    }

    // Implementa métodos para dibujar la cuadrícula y el cuadro especial
    

    // Implementa métodos para dibujar el proceso de adoquinamiento paso a paso
    
    
}
