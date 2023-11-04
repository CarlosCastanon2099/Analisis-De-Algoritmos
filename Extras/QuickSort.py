"""
Versión de Quick Sort que toma como pivote al elemento A[(first + last)div2]
"""
num_partition = 0

def quick_sort1(arr, first, last):
    global num_partition
    if first < last:
        pivot_index = partition(arr, first, last)
        # Ahora imprimiremos la iteracion en la que estamos
        num_partition += 1
        print(f"Partición {num_partition}:  {arr[first:pivot_index+1]} | {arr[pivot_index]} | {arr[pivot_index+1:last+1]}")
        quick_sort1(arr, first, pivot_index)
        quick_sort1(arr, pivot_index + 1, last)


def partition(arr, first, last):
    pivot_index = (first + last) // 2
    pivot_value = arr[pivot_index]
    left = first
    right = last

    while True:
        while arr[left] < pivot_value:
            left += 1
        while arr[right] > pivot_value:
            right -= 1
        if left >= right:
            break
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return right

# Ejemplo de uso
arr = [99, 32, 89, 45, 73, 28, 91, 12, 64, 78, 53, 2, 1, 24, 42, 60, 86, 19, 5, 95, 8, 50, 56]

print("Quick Sort 1: \n")

print(f"Arreglo original: {arr}")  # Imprime el arreglo original

quick_sort1(arr, 0, len(arr) - 1)

print(f"Arreglo ordenado: {arr}")  # Imprime el arreglo ordenado



"""
Versión de Quick Sort que toma como pivote al elemento que resulta ser la mediana de:
A[first], A[(first + last)div2], A[last]
"""
num_partition2 = 0
def quick_sort2(arr, first, last):
    global num_partition2
    if first < last:
        pivot_index = partition2(arr, first, last)
        num_partition2 += 1
        print(f"Partición {num_partition2}: {arr[first:pivot_index+1]} | {arr[pivot_index]} | {arr[pivot_index+1:last+1]}")
        quick_sort2(arr, first, pivot_index)
        quick_sort2(arr, pivot_index + 1, last)

def partition2(arr, first, last):
    mid = (first + last) // 2
    pivot_index = median_of_three(arr, first, mid, last)
    pivot_value = arr[pivot_index]
    left = first
    right = last

    while True:
        while arr[left] < pivot_value:
            left += 1
        while arr[right] > pivot_value:
            right -= 1
        if left >= right:
            break
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return right

def median_of_three(arr, first, mid, last):
    if arr[first] <= arr[mid] <= arr[last] or arr[last] <= arr[mid] <= arr[first]:
        return mid
    elif arr[mid] <= arr[first] <= arr[last] or arr[last] <= arr[first] <= arr[mid]:
        return first
    else:
        return last

# Ejemplo de uso
arr2 = [99, 32, 89, 45, 73, 28, 91, 12, 64, 78, 53, 2, 1, 24, 42, 60, 86, 19, 5, 95, 8, 50, 56]

print("\n -------------------------------------------------------------------------------- \n ")

print("Quick Sort 2: \n")

print(f"Arreglo original: {arr2}")  # Imprime el arreglo original

quick_sort2(arr2, 0, len(arr2) - 1)

print(f"Arreglo ordenado: {arr2}")  # Imprime el arreglo ordenado

