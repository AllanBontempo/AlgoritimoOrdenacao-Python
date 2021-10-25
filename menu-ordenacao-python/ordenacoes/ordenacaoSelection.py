def ordenar(array, ordenacao):
    for i in range(len(array)):
        auxiliar = i
        for j in range(i+1, len(array)):
            if ordenacao == 'c':
                if array[auxiliar] > array[j]:
                    auxiliar = j
            elif ordenacao == 'd':
                if array[auxiliar] < array[j]:
                    auxiliar = j
        
        array[i], array[auxiliar] = array[auxiliar], array[i]
    print(array)