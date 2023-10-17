# Implementacion de shell sort en python
# Esta implementacion muestra paso a paso como se va ordenando el arreglo

def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            # print("i: ",i)
            # print("h : ",gap)
            temp = arr[i]
            j = i
            while  j >= gap and arr[j-gap] >temp:
                print("j: ",j)
                print("h: ",gap)
                arr[j] = arr[j-gap]
                j -= gap
                print(arr)
                print("\n")
            arr[j] = temp
        gap //= 2
    return arr

def shell_sort(arr):
    n = len(arr)
    h = 8  # El valor de h inicial en la primera iteración

    while h > 0:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        h = h // 2

# Implementacion de shell sort en python
# Esta implementacion muestra paso a paso como se va ordenando el arreglo
def shell_sort_with_output(arr):
    n = len(arr)
    h = n // 2  # El valor de h inicial en la primera iteración
    print("Arreglo Original :", arr)

    while h > 0:
        print("\n")
        print(f"i = {n // h}")
        print(f"h = {h}\n")

        print("A :", arr)

        for i in range(h):
            
            subsequence = arr[i::h]
            subsequence_str1 = " ".join(map(str, subsequence))
            arr[i::h] = subsequence
            print(f"S{i + 1}:[{subsequence_str1}]")


            subsequence.sort()
            arr[i::h] = subsequence
            subsequence_str = " ".join(map(str, subsequence))
            print(f"S{i + 1}:[{subsequence_str}]")

        h = h // 2

# Secuencia original
S = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]


# Implementacion de shell sort usando incrementos de Hibbard
# Usaremos el codigo de shell_sort_with_output para solo hacerle la
# modificacion de los incrementos de Hibbard
def shell_sort_hibbard_with_output(arr):
    n = len(arr)
    h = 1  # El valor de h inicial en la primera iteración
    k = 1
    print("---------------------------Hibbard-----------------------------")
    while h < n:
        h = (2 ** k) - 1
        k += 1

    while h > 0:
        print("\n")
        print("A :", arr)

        print(f"i = {n // h}")
        print(f"h = {h}\n")

        

        for i in range(h):
            subsequence = arr[i::h]
            subsequence_str1 = " ".join(map(str, subsequence))
            arr[i::h] = subsequence
            print(f"S{i + 1}:[{subsequence_str1}]")

            subsequence.sort()
            arr[i::h] = subsequence
            subsequence_str = " ".join(map(str, subsequence))
            print(f"S{i + 1}:[{subsequence_str}]")

        k -= 1
        h = 2 ** k - 1
        


# arr2 = [ 1,9,2,10,3,11,4,12,5,13,6,14,7,15,8,16 ]

# Llamada a la función Shell Sort con salida

# Arreglo de 35 digitos diferentes en el que Shell Sort realiza menos operaciones que la version de Hibbard
arregloBueno1 = [ 1,9,2,10,3,11,4,12,5,13,6,14,7,15,8,16,17,25,18,26,19,27,20,28,21,29,22,30,23,31,24,32,33,34,35 ]
arregloBueno2 = [ 1,9,2,10,3,11,4,12,5,13,6,14,7,15,8,16,17,25,18,26,19,27,20,28,21,29,22,30,23,31,24,32,33,34,35 ]

lista35 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

beta1 = [ 101,102,103,104,3,11,4,12,5,13,6,14,7,15,8,116,117,118,119,120,19,27,20,28,21,29,22,30,23,31,131,132,133,134,135 ]
beta2 = [ 101,102,103,104,3,11,4,12,5,13,6,14,7,15,8,116,117,118,119,120,19,27,20,28,21,29,22,30,23,31,131,132,133,134,135 ]


print(shell_sort_with_output(beta1))
print(shell_sort_hibbard_with_output(beta2))



#arr1 = [503,87,512,61,908,170,897,275,653,426,154,509,612,677,765,703]
#
#print(arr1)
#print("----------------------------------------------------------")
#print(shellSort(arr1))
