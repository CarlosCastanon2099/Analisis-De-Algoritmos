"""""
def radix_sort_lsd_hex(arr):
    # Encuentra la longitud máxima de los números hexadecimales en el arreglo
    max_len = max(len(hex(num)) - 2 for num in arr)  # Resta 2 para eliminar '0x' del formato hexadecimal

    # Aplica el Radix Sort LSD por cada posición del dígito
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(16)]  # 16 cubetas para dígitos hexadecimales (0-9, A-F)

        for num in arr:
            # Obtiene el dígito en la posición i (de derecha a izquierda)
            digit = int(hex(num)[-1 - i], 16)
            buckets[digit].append(num)

        arr = [num for bucket in buckets for num in bucket]

    return arr

# Ejemplo de uso con números hexadecimales
hex_numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca]
sorted_hex_numbers = radix_sort_lsd_hex(hex_numbers)


print("Arreglo original:")
print(hex_numbers)

print("\nArreglo ordenado:")
print(sorted_hex_numbers)

"""""


def radix_sort_lsd_hex_with_output(arr):
    max_len = max(len(hex(num)) - 2 for num in arr)
    
    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(16)]
        
        print(f"Iteración: {max_len - i}")
        print("Elementos asignados en los cubos:")
        print(" _ ")
        print("|B|")
        for num in arr:
            digit = int(hex(num)[-1 - i], 16)
            buckets[digit].append(num)
            
            
        for j, bucket in enumerate(buckets):

            print("---")
            hex_bucket = [hex(num) for num in bucket]
            print(f"|{j}| = {hex_bucket}")
            print("---")
        
        arr = [num for bucket in buckets for num in bucket]
    
    return arr

# Ejemplo de uso con números hexadecimales
# hex_numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca]
hex_numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca,    
               0x1b4f, 0x9f8d, 0x8b23, 0xd590, 0x2e16,    
               0x3c97, 0x7261, 0xf1d8, 0x5a42, 0x846e,    
               0x17f3, 0xcba5, 0x65fd, 0x92e7, 0x4d8c,    
               0x369f, 0xfeca, 0xae57, 0x81b9, 0xd241]

print("Arreglo original:")
print([hex(num) for num in hex_numbers])
print("\nProceso de ordenamiento:")

sorted_hex_numbers = radix_sort_lsd_hex_with_output(hex_numbers)

print("\nArreglo ordenado:")
print([hex(num) for num in sorted_hex_numbers])

