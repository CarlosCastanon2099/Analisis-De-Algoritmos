import sys
import glob
import os
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import numpy as np


size_of_grid = 0
b = 0
a = 0
cnt = 0
arr = [[0 for i in range(128)] for j in range(128)]



def place(x1, y1, x2, y2, x3, y3):
    global cnt
    cnt += 1
    arr[x1][y1] = cnt
    arr[x2][y2] = cnt
    arr[x3][y3] = cnt





def tile(n, x, y):
    global cnt
    r = 0
    c = 0
    if n == 2:
        cnt += 1
        for i in range(n):
            for j in range(n):
                if arr[x + i][y + j] == 0:
                    arr[x + i][y + j] = cnt

        return 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != 0:
                r = i
                c = j
    if r < x + n / 2 and c < y + n / 2:
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))

    elif r >= x + int(n / 2) and c < y + int(n / 2):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2),
              x + int(n / 2) - 1, y + int(n / 2) - 1)

    elif r < x + int(n / 2) and c >= y + int(n / 2):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2),
              x + int(n / 2) - 1, y + int(n / 2) - 1)

    elif r >= x + int(n / 2) and c >= y + int(n / 2):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1,
              x + int(n / 2) - 1, y + int(n / 2) - 1)

    tile(int(n / 2), x, y + int(n / 2))
    tile(int(n / 2), x, y)
    tile(int(n / 2), x + int(n / 2), y)
    tile(int(n / 2), x + int(n / 2), y + int(n / 2))

    return 0

# Many thanks to https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/

def plot_grid(grid, colors, special):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(0, size_of_grid + 1, 1))
    ax.set_yticks(np.arange(0, size_of_grid + 1, 1))
    ax.grid(which="both", color="black", linewidth=2)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for i in range(size_of_grid):
        for j in range(size_of_grid):
            if (i, j) == special:
                color = 'black'  # Special square color
            else:
                color = colors[grid[i][j]]

            rect = plt.Rectangle((j, size_of_grid - 1 - i), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    plt.gca().invert_yaxis()  # Invert y-axis to match the array indexing
    #plt.show()  Descomenta esto si deseas veer TODAS las imagenes generadas por el programa (son muchas) en ventanas pop-out


size_of_grid = 2
a = 0
b = 0
arr[a][b] = -1
tile(size_of_grid, 0, 0)

# Mapping of numbers to colors
color_map = {0: 'white', -1: 'black'}

for i in range(1, cnt + 1):
    color_map[i] = plt.cm.get_cmap('tab20')(i / cnt)  # Use 'tab20' colormap

# Display the grid on the console
for i in range(size_of_grid):
    for j in range(size_of_grid):
        print(arr[i][j], end=" ")
    print()

# Plot the grid using matplotlib
plot_grid(arr, color_map, (a, b))


# Save the grid as a PNG image
def save_grid(grid, colors, special, filename):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(0, size_of_grid + 1, 1))
    ax.set_yticks(np.arange(0, size_of_grid + 1, 1))
    ax.grid(which="both", color="black", linewidth=2)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for i in range(size_of_grid):
        for j in range(size_of_grid):
            if (i, j) == special:
                color = 'black'  # Special square color
            else:
                color = colors[grid[i][j]]

            rect = plt.Rectangle((j, size_of_grid - 1 - i), 1, 1, linewidth=1, edgecolor='black', facecolor=color)
            ax.add_patch(rect)

    plt.gca().invert_yaxis()  # Invert y-axis to match the array indexing
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


save_grid(arr, color_map, (a, b), 'adoquinamientoFinal.png')


# Funcion auxliar que dado un numero de entrada n, eleva 2 a la n
def potenciadeDos(n):
    return 2 ** n


# Funcion auxiliar que genera un archivo .png de la imagen actual (similar a la funcion save_grid)
def generate_image():
    global cnt
    color_map = {0: 'white', -1: 'black'}

    for i in range(1, cnt + 1):
        color_map[i] = plt.cm.get_cmap('tab20')(i / cnt)  # Use 'tab20' colormap

    ## Display the grid on the console
    #for i in range(size_of_grid):
    #    for j in range(size_of_grid):
    #        print(arr[i][j], end=" ")
    #    print()

    # Plot the grid using matplotlib
    plot_grid(arr, color_map, (a, b))

    # Save the grid as a PNG image
    save_grid(arr, color_map, (a, b), 'adoquinamiento' + str(cnt) + '.png')

# Funcion que usa a generate_image() para generar un gif usando todas las imagenes generadas por generate_image() 
# una vez generado el gif se borran todas las imagenes generadas por generate_image()
def generate_gif():
    global cnt
    images = []
    # guardamos todas las imagenes generadas por generate_image() en una lista, tengamos en cuenta que el nombre de las imagenes
    # generadas por generate_image() es 'adoquinamiento' + str(cnt) + '.png' por lo que podemos usar un ciclo for para recorrer
    # todas las imagenes generadas que cumplan con ese patron de nombre (es decir, podria no existir el archivo adoquinamiento4.png pero si
    # existir el archivo adoquinamiento5.png, por lo que el ciclo for solo recorrera los archivos que existan)
    for filename in glob.glob('adoquinamiento*.png'):
        images.append(imageio.imread(filename))
    
    # Ahora ordenamos las imagenes que se hayan generado por generate_image() para que se muestren en orden
    for filename in sorted(glob.glob('adoquinamiento*.png'), key=os.path.getmtime):
        images.append(imageio.imread(filename))

    # Generamos el gif usando las imagenes que se hayan generado por generate_image()
    imageio.mimsave('adoquinamientoPasoaPaso.gif', images)

    # Borramos todas las imagenes generadas por generate_image()
    for filename in glob.glob('adoquinamiento*.png'):
        os.remove(filename)



# Ahora tenemos el metodo tile2 el cual funciona exactamente igual que el metodo tile, pero en este caso lo modificaremos para
# que genere una imagen por cada llamada recursiva que haga, de esta manera, al finalizar el programa, tendremos una imagen
# por cada llamada recursiva que se hizo, y asi podremos ver como se va formando el adoquinamiento
def tile2(n, x, y):
    global cnt
    r = 0
    c = 0
    if n == 2:
        cnt += 1
        generate_image()
        for i in range(n):
            for j in range(n):
                if arr[x + i][y + j] == 0:
                    arr[x + i][y + j] = cnt
        generate_image()
        return 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != 0:
                r = i
                c = j
    generate_image()
    if r < x + n / 2 and c < y + n / 2:
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))

    elif r >= x + int(n / 2) and c < y + int(n / 2):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2),
              x + int(n / 2) - 1, y + int(n / 2) - 1)

    elif r < x + int(n / 2) and c >= y + int(n / 2):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2),
              x + int(n / 2) - 1, y + int(n / 2) - 1)

    elif r >= x + int(n / 2) and c >= y + int(n / 2):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1,
              x + int(n / 2) - 1, y + int(n / 2) - 1)

    tile2(int(n / 2), x, y + int(n / 2))
    tile2(int(n / 2), x, y)
    tile2(int(n / 2), x + int(n / 2), y)
    tile2(int(n / 2), x + int(n / 2), y + int(n / 2))

    return 0


size_of_grid = 2
a = 0
b = 0
arr[a][b] = -1
tile2(size_of_grid, 0, 0)

# Mapping of numbers to colors
color_map = {0: 'white', -1: 'black'}

for i in range(1, cnt + 1):
    color_map[i] = plt.cm.get_cmap('tab20')(i / cnt)  # Use 'tab20' colormap

# Display the grid on the console
#for i in range(size_of_grid):
#    for j in range(size_of_grid):
#        print(arr[i][j], end=" ")
#    print()

# Plot the grid using matplotlib
#plot_grid(arr, color_map, (a, b))

#save_grid(arr, color_map, (a, b), 'adoquinamientoFinal.png')



# Funcion auxiliar que ajusta los fps de un gif
def adjust_gif_fps(filename, fps):
    reader = imageio.get_reader(filename)
    fps = float(fps)
    writer = imageio.get_writer('adoquinamientoPasoaPaso.gif', fps=fps)
    for im in reader:
        writer.append_data(im)
    writer.close()



# Use of the program: python3 Programa01A.py <n> 
# where <n> is the size of the grid (must be a power of 2)
# Example: python3 Programa01A.py 8

if __name__ == '__main__':
    if len(sys.argv) == 2:
        size_of_grid = int(sys.argv[1])
        if size_of_grid != 0:
            size_of_grid = potenciadeDos(size_of_grid)
            a = 0
            b = 0
            arr[a][b] = -1
            tile2(size_of_grid, 0, 0)

            # Mapping of numbers to colors
            color_map = {0: 'white', -1: 'black'}

            for i in range(1, cnt + 1):
                color_map[i] = plt.cm.get_cmap('tab20')(i / cnt)  # Use 'tab20' colormap

            # Display the grid on the console
            for i in range(size_of_grid):
                for j in range(size_of_grid):
                    print(arr[i][j], end=" ")
                print()

            # Plot the grid using matplotlib
            plot_grid(arr, color_map, (a, b))

            # Save the grid as a PNG image
            save_grid(arr, color_map, (a, b), 'ElAdoquinamientoFinal.png')

            # Generamos el Gif 
            generate_gif()

            # Ajustamos los fps del gif
            adjust_gif_fps('adoquinamientoPasoaPaso.gif', 1)



        else:
            print('Error: <n> must be a power of 2')
    else:
        print('Error: invalid number of arguments')