import sys

size_of_grid = 0
b = 0
a = 0
cnt = 0
arr = [[0 for i in range(128)] for j in range(128)]
 
def place(x1, y1, x2, y2, x3, y3):
    global cnt
    cnt += 1
    arr[x1][y1] = cnt;
    arr[x2][y2] = cnt;
    arr[x3][y3] = cnt;
     
def tile(n, x, y):
    global cnt
    r = 0
    c = 0
    if (n == 2):
        cnt += 1
        for i in range(n):
            for j in range(n):
                if(arr[x + i][y + j] == 0):
                    arr[x + i][y + j] = cnt
        return 0;    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (arr[i][j] != 0):
                r = i
                c = j  
    if (r < x + n / 2 and c < y + n / 2):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2))
     
    elif(r >= x + int(n / 2) and c < y + int(n / 2)):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
     
    elif(r < x + int(n / 2) and c >= y + int(n / 2)):
        place(x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2), y + int(n / 2), x + int(n / 2) - 1, y + int(n / 2) - 1)
     
    elif(r >= x + int(n / 2) and c >= y + int(n / 2)):
        place(x + int(n / 2) - 1, y + int(n / 2), x + int(n / 2), y + int(n / 2) - 1, x + int(n / 2) - 1, y + int(n / 2) - 1)
     
    tile(int(n / 2), x, y + int(n / 2));
    tile(int(n / 2), x, y);
    tile(int(n / 2), x + int(n / 2), y);
    tile(int(n / 2), x + int(n / 2), y + int(n / 2)); 
     
    return 0
 
size_of_grid = 8
a = 0
b = 0
arr[a][b] = -1
tile(size_of_grid, 0, 0)
 
for i in range(size_of_grid):
    for j in range(size_of_grid):
        print(arr[i][j], end=" ")
    print()
 
# The above code is contributed by rag2127
# https://www.geeksforgeeks.org/tiling-problem-using-divide-and-conquer-algorithm/
    


# Ahora establecemos el metodo main
# Para invocar el programa debemosm ejecutar: python Programa01.py <n>
# Donde n es el tamaño de la matriz a generar y debe ser potencia de 2

if __name__ == "__main__":
    # Obtenemos el tamaño de la matriz
    size_of_grid = int(sys.argv[1])
    # Inicializamos la matriz
    arr = [[0 for i in range(size_of_grid)] for j in range(size_of_grid)]
    # Inicializamos el contador
    cnt = 0
    # Inicializamos el primer cuadrante
    a = 0
    b = 0
    arr[a][b] = -1
    # Invocamos el metodo tile
    tile(size_of_grid, 0, 0)
    # Imprimimos la matriz
    for i in range(size_of_grid):
        for j in range(size_of_grid):
            print(arr[i][j], end=" ")
        print() 