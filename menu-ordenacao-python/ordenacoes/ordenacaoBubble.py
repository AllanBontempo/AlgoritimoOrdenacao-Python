def ordenar(array, ordenacao):
    tamanho = len(array)
    for i in range(tamanho-1):
        for j in range(0, tamanho-i-1):
            if ordenacao == 'c':
                if array[j] > array[j+1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            elif ordenacao == 'd':
                if array[j] < array[j+1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    print(array)

