def bucket_sort(arr):
    # Encuentra el valor máximo en el arreglo
    max_val = max(arr)
    # Calcula el número de cubetas
    # num_buckets = max_val // 10 + 1  #  para un rango de 0 a 99 - A) (Y Diez cubetas)
    # num_buckets = max_val // 100 + 1 #  para un rango de 0 a 999 - B)  (Y Diez cubetas)
    num_buckets = (max_val // 100 + 1) // 2 #  para un rango de 0 a 999 - C)  (Y Cinco cubetas)


    # Inicializa las cubetas
    buckets = [[] for _ in range(num_buckets)]

    # Coloca los elementos en las cubetas
    for num in arr:
        # bucket_index = num // 10  # para un rango de 0 a 99  - A) (Y Diez cubetas)
        # bucket_index = num // 100 # para un rango de 0 a 999 - B) (Y Diez cubetas)
        bucket_index = (num // 100) // 2 # para un rango de 0 a 999 - C) (Y Cinco cubetas)
        buckets[bucket_index].append(num)

    sorted_array = []

    print("Iteracion: 01")
    print("Elementos asignados en el bucket")
    print("\n")
    print(" _ ")
    print("|B|")
    for i, bucket in enumerate(buckets):

        print("---")
        print(f"|{i}| = {bucket}")
        print("---")

    # Ordena y concatena las cubetas
    for bucket in buckets:
        if bucket:
            bucket.sort()
            sorted_array.extend(bucket)

    print("\n\nIteracion: 02")
    print("Elementos del bucket ordenados")
    print("\n")
    print(" _ ")
    print("|B|")
    for i, bucket in enumerate(buckets):

        print("---")
        print(f"|{i}| = {bucket}")
        print("---")

    return sorted_array




# Ejemplo de uso
# S = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
S = [764, 235, 129, 492, 631, 845, 376, 508, 347, 912, 586, 419, 753, 624, 187, 265, 978, 341, 562, 829, 154, 496, 723, 618, 295, 871, 430, 569, 324, 784]


print("El arreglo original es:")
print(f"S = {S}")
sorted_S = bucket_sort(S)

print("\nEl arreglo ordenado es:")
print(f"S' = {sorted_S}")