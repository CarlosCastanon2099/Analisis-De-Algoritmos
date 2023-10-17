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

    while h > 0:
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

        h = h // 2

# Secuencia original
S = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]

# Llamada a la función Shell Sort con salida
shell_sort_with_output(S)

# Imprimir la secuencia ordenada
print(S)

#arr1 = [503,87,512,61,908,170,897,275,653,426,154,509,612,677,765,703]
#arr2 = [ 1,9,2,10,3,11,4,12,5,13,6,14,7,15,8,16 ]
#print(arr1)
#print("----------------------------------------------------------")
#print(shellSort(arr1))
