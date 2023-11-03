# numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca]
hex_numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca,    
               0xea5f, 0x9f8d, 0x8b23, 0xd590, 0x2e16,    
               0x3c97, 0x7261, 0xf1d8, 0x5a42, 0x846e,    
               0x2f43, 0xcba5, 0x65fd, 0x92e7, 0x4d8c,    
               0x369f, 0xfeca, 0xae57, 0x81b9, 0xd241]

print("\n Arreglo original: \n" )
print([hex(num) for num in hex_numbers])

print("\n Arreglo Decimal \n")
print(hex_numbers)

# Version que muestra cada iteracion con los numeros en hexadecimal
def radixLSDSort(arr):

    num_buckets = 10 


    # Inicializa las cubetas
    buckets = [[] for _ in range(num_buckets)]

    # Coloca los elementos en las cubetas iniciando por su digito menos significativo
    for num in arr:
        bucket_index = num % 10 
        buckets[bucket_index].append(num)
    
    sorted_array = []

    # Vamos a tener tantas iteraciones como el numero de digitos del numero mas grande
    max_len = max(len(hex(num)) - 2 for num in arr)

    for i in range(max_len - 1, -1, -1):
        buckets = [[] for _ in range(16)]
        
        print(f"Iteración: {max_len - i}")
        print("Elementos asignados en los cubos:")
        print(" _ ")
        print("|B|")
        for num in arr:
            digit = int(hex(num)[2 + i], 16)
            buckets[digit].append(num)
            
            
        for j, bucket in enumerate(buckets):

            hex_bucket = [hex(num) for num in bucket]
            print(f"|{j}| = {hex_bucket}")
            
        arr = [num for bucket in buckets for num in bucket]

    return arr



sorted_hex_numbers = radixLSDSort(hex_numbers)

print("\nArreglo ordenado:")
print([hex(num) for num in sorted_hex_numbers])

# Ahora Imrprimimos los numeros en decimal
print("\nArreglo ordenado:")
print([num for num in sorted_hex_numbers])


# Version que muestra cada iteracion con los numeros en decimal
# Esta version recibe una lista de numeros en decimal
# Y por ende todas las iteraciones se muestran en decimal
# hex_numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca,    
#               0xea5f, 0x9f8d, 0x8b23, 0xd590, 0x2e16,    
#               0x3c97, 0x7261, 0xf1d8, 0x5a42, 0x846e,    
#               0x2f43, 0xcba5, 0x65fd, 0x92e7, 0x4d8c,    
#               0x369f, 0xfeca, 0xae57, 0x81b9, 0xd241]
dec_numbers = [58999, 41958, 17601, 28140, 22474, 59999, 
               40845, 35619, 54672, 11798, 15511, 29281, 
               61912, 23106, 33902, 12099, 52133, 26109, 
               37607, 19852, 13983, 65226, 44631, 33209, 53825]


def radixLSDSortDecimal(arr):
        num_buckets = 10 
        # Inicializa las cubetas
        buckets = [[] for _ in range(num_buckets)]
    
        # Coloca los elementos en las cubetas iniciando por su digito menos significativo
        for num in arr:
            bucket_index = num % 10 
            buckets[bucket_index].append(num)
        
        sorted_array = []
        # Vamos a tener tantas iteraciones como el numero de digitos del numero mas grande
        max_len = max(len(str(num)) for num in arr)
    
        for i in range(max_len - 1, -1, -1):
            buckets = [[] for _ in range(16)]
            
            print(f"Iteración: {max_len - i}")
            print("Elementos asignados en los cubos:")
            print(" _ ")
            print("|B|")
            for num in arr:
                digit = int(str(num)[i])
                buckets[digit].append(num)
                
                
            for j, bucket in enumerate(buckets):
    
                hex_bucket = [num for num in bucket]
                print(f"|{j}| = {hex_bucket}")
                
            arr = [num for bucket in buckets for num in bucket]
    
        return arr


print("\nArreglo ordenado:")
print(radixLSDSortDecimal(dec_numbers))
