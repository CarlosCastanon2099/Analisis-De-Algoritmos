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
    plt.show()


size_of_grid = 8
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


save_grid(arr, color_map, (a, b), 'grid.png')

# Use of the program: python3 Programa01A.py <n> 
# where <n> is the size of the grid (must be a power of 2)
# Example: python3 Programa01A.py 8

if __name__ == '__main__':
    if len(sys.argv) == 2:
        size_of_grid = int(sys.argv[1])
        if size_of_grid & (size_of_grid - 1) == 0:
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
            save_grid(arr, color_map, (a, b), 'grid.png')
        else:
            print('Error: <n> must be a power of 2')
    else:
        print('Error: invalid number of arguments')
