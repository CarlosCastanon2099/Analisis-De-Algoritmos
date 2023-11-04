def bucket_sort(numbers, index):
    buckets = [[] for _ in range(10)]
    for number in numbers:
        digit = (number // 10**index) % 10
        buckets[digit].append(number)
    sorted_numbers = [number for bucket in buckets for number in sorted(bucket)]
    print(f'Iteración {index}: ')
    print(f'Elementos asignados en los cubos: ')
    print(' _ ')
    print('|B|')
    for i, bucket in enumerate(buckets):
        print(f'|{i}| = {bucket}')
    print(f'Nuevo Arreglo: {sorted_numbers}')

    return sorted_numbers

def radix_msd_sort(numbers, index=4):
    if len(numbers) <= 1 or index < 0:
        return numbers
    sorted_numbers = bucket_sort(numbers, index)
    return [number for bucket in [radix_msd_sort([num for num in sorted_numbers if (num // 10**index) % 10 == digit], index-1) for digit in range(10)] for number in bucket]

dec_numbers = [58999, 41958, 17601, 28140, 22474, 59999, 
               40845, 35619, 54672, 11798, 15511, 29281, 
               61912, 23106, 33902, 12099, 52133, 26109, 
               37607, 19852, 13983, 65226, 44631, 33209, 53825]

radix_msd_sort(dec_numbers)


# Ahora implementamos la version para numeros hexadecimales
# Esta version recibe una lista de numeros en hexadecimal
# Y por ende todas las iteraciones se muestran en hexadecimal
hex_numbers = [0xe677, 0xa3e6, 0x44c1, 0x6dec, 0x57ca,    
               0xea5f, 0x9f8d, 0x8b23, 0xd590, 0x2e16,    
               0x3c97, 0x7261, 0xf1d8, 0x5a42, 0x846e,    
               0x2f43, 0xcba5, 0x65fd, 0x92e7, 0x4d8c,    
               0x369f, 0xfeca, 0xae57, 0x81b9, 0xd241]

def bucket_sort_hex(numbers, index):
    buckets = [[] for _ in range(16)]
    for number in numbers:
        digit = (number // 16**index) % 16
        buckets[digit].append(number)
    sorted_numbers = [number for bucket in buckets for number in sorted(bucket)]
    print(f'Iteración {index}: ')
    print(f'Elementos asignados en los cubos: ')
    print(' _ ')
    print('|B|')
    for i, bucket in enumerate(buckets):
        hex_bucket = [hex(num) for num in bucket]
        print(f'|{i}| = {hex_bucket}')
    print(f'Nuevo Arreglo: {sorted_numbers}')
    print([hex(num) for num in sorted_numbers])

    return sorted_numbers

def radix_msd_sort_hex(numbers, index=3):
    if len(numbers) <= 1 or index < 0:
        return numbers
    sorted_numbers = bucket_sort_hex(numbers, index)
    return [number for bucket in [radix_msd_sort_hex([num for num in sorted_numbers if (num // 16**index) % 16 == digit], index-1) for digit in range(16)] for number in bucket]

radix_msd_sort_hex(hex_numbers)